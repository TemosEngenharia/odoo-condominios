# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VirdiTerminais(models.Model):
    _name = 'occ.virdi'
    _description = 'Equipamentos Virdi'
    _order = 'terminal_id'
    _table = 'occ_virdi'
    terminal_id = fields.Char('ID do terminal', size=8, required=True)
    terminal_ip = fields.Char('IP do terminal', size=15, require=True)
    terminal_port = fields.Char('Porta socket terminal', size=5, require=True)
    terminal_status = fields.Boolean('Cancela', default=True)

    @api.multi
    def do_open_lock(self):
        self.terminal_status = False
        return True
