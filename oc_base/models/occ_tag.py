# -*- coding: utf-8 -*-
from openerp import models, fields


class OccTAG(models.Model):
    _name = 'occ.tag'
    _description = 'Detalhes das TAGs'
    _order = 'name'
    _table = 'occ_tag'
    _sql_constraints = [('occ.tag', 'UNIQUE (name)',
                         'As TAGs devem ser únicas')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='TAG', size=6, required=True)
    tipo = fields.Selection([('carro', 'TAG Carro'), ('moto', 'TAG Moto')],
                            "Tipo", default='carro', required=True)
    veiculo_ids = fields.One2many('occ.veiculo', 'tag_id', 'Veículo')
    vaga_carro_ids = fields.Many2many('occ.vaga.carro', 'occ_tag_carro_rel',
                                      'tag_ids', 'vaga_carro_ids',
                                      string='Vagas Carro')
    vaga_moto_ids = fields.Many2many('occ.vaga.moto', 'occ_tag_moto_rel',
                                     'tag_ids', 'vaga_moto_ids',
                                     string='Vagas Moto')
