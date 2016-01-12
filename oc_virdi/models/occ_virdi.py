# -*- coding: utf-8 -*-
from openerp import models, fields, api


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

    @api.multi
    def do_open_lock(self):
        self.terminal_status = 'open'
        return True


class VirdiAcesso(models.Model):
    _name = 'occ.acesso'
    _description = 'Lista dos acessos'
    _order = 'horario'
    _table = 'occ_acesso'
    image = fields.Binary('Foto')
    morador = fields.Char('Morador', size=45, required=True)
    placa = fields.Char('Placa', size=8, required=True)
    horario = fields.Char('Horário', required=True)
    apto = fields.Char('Apartamento', size=5, required=True)
    sentido = fields.Selection([('in', 'Entrada'), ('out', 'Saída'),
                                ('erro', 'Erro')], "Tipo", default='in',
                               required=True)
    status = fields.Char('Situação', required=True)
