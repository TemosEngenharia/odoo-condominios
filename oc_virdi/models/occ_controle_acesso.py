# -*- coding: utf-8 -*-
from openerp import models, fields
from __builtin__ import True


class VirdiTerminais(models.Model):
    _name = 'occ.virdi'
    _description = 'Equipamentos Virdi'
    _order = 'terminal_id'
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


class ControleAcesso(models.Model):
    _name = 'occ.controle.acesso'
    _description = 'Tabela de Controle de Acesso'
    _table = 'occ_controle_acesso'
    horario = fields.Char('Horário', required=True)
    sentido = fields.Selection([('in', 'Entrada'), ('out', 'Saída')],
                               "Sentido", default='in',
                               required=True)
    morador = fields.Many2one('occ.morador', 'Morador',
                              required=True)
    placa = fields.Many2one('occ.veiculos', 'Placa',
                            required=True)
    status = fields.Char('Situação', required=True)

    def abrir_cancela_entrada(self):
        self.env.invalidate_all()
        self.env.cr.execute("UPDATE occ_virdi SET terminal_status = 'open' \
                            WHERE terminal_tipo = 'in'")
        self.env.invalidate_all()
        return True

    def abrir_cancela_saida(self):
        self.env.invalidate_all()
        self.env.cr.execute("UPDATE occ_virdi SET terminal_status = 'open' \
                            WHERE terminal_tipo = 'out'")
        self.env.invalidate_all()
        return True
