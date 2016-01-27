# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VirdiTerminais(models.Model):
    _name = 'occ.virdi'
    _description = 'Equipamentos Virdi'
    _order = 'terminal_status'
    _table = 'occ_virdi'
    terminal_id = fields.Char('ID do terminal', size=8, required=True)
    terminal_ip = fields.Char('IP do terminal', size=15, require=True)
    terminal_port = fields.Char('Porta socket terminal', size=5,
                                readonly=True, require=True)
    terminal_tipo = fields.Selection([('in', 'Entrada'), ('out', 'Saída')],
                                     "Tipo", default='in', required=True)
    terminal_status = fields.Selection([('open', 'Aberta'),
                                        ('close', 'Fechada')],
                                       "Estado", default='close',
                                       required=True)

    @api.multi
    def do_open_lock(self):
        self.terminal_status = 'open'
        return True


class ControleAcesso(models.Model):
    _name = 'occ.controle.acesso'
    _description = 'Tabela de Controle de Acesso'
    _table = 'occ_controle_acesso'
    _order = 'horario desc'
    horario = fields.Char('Horário')
    horario_2 = fields.Date()
    sentido = fields.Selection([('in', 'Entrada'), ('out', 'Saída')],
                               "Sentido")
    morador = fields.Many2one('occ.morador', 'Morador')
    placa = fields.Many2one('occ.veiculo', 'Placa')
    placa_2 = fields.Char('Placa_2')
    status = fields.Char('Situação')

    @api.multi
    def abrir_cancela(self):
        sql = """
            UPDATE occ_virdi SET terminal_status = 'open'
                WHERE terminal_tipo = %s;
        """
        self.env.cr.execute(sql, (self.sentido, ))
        self.env.invalidate_all()
        return True

    @api.onchange('placa_2')
    def preencher_dados(self):
        if self.placa_2:
            sql = """
                SELECT id FROM occ_veiculos WHERE name = %s;
                """
            self.env.cr.execute(sql, (self.placa_2, ))
