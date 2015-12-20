# -*- coding: utf-8 -*-
from openerp import models, fields, api


class VirdiTAG(models.Model):
    _inherit = 'occ.tag'

    @api.depends('name')
    def SearchTAG(self, tag):
        if not self.search([('name', '=', tag)]):
            return False
        else:
            return True


class OccVirdi(models.Model):
    _name = 'occ.virdi'
    _description = 'Detalhes das Controladoras'
    _order = 'name'
    _table = 'occ_virdi'
    _sql_constraints = [
                        ('occ.virdi', 'unique (name)',
                         'Já existe uma controladora com este ID!')
                       ]
    name = fields.Char('ID', size=8, required=True)
    ip_addr = fields.Char('IP', size=12, require=True)
    modelo = fields.Char('Modelo', size=4, require=True)
    local = fields.Selection([('gate_morador', 'Portão Morador'),
                              ('cancela_entrada', 'Cancela de Entrada'),
                              ('cancela_saida', 'Cancela de Saída')],
                             "Local", default='gate_morador', require=True)


class OccVirdiAcessos(models.Model):
    _name = 'occ.virdiacessos'
    _description = 'Registros das tentitativas e sucessos de acesso'
    _order = 'data_acesso'
    _table = 'occ_virdiacessos'
    status = fields.Selection([('autorizado', 'Acesso Liberado'),
                               ('negado', 'Acesso Negado')],
                              "Situação")
