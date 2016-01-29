# -*- coding: utf-8 -*-
from openerp import models, fields


class OccVeiculo(models.Model):
    _name = 'occ.veiculo'
    _description = 'Detalhes das Veiculos'
    _order = 'name'
    _table = 'occ_veiculos'
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name)',
                         'Placa já cadastrada')]
    _sql_constraints = [('occ.veiculo', 'UNIQUE (name,tag_id)',
                         'Um veículo deve ter somente uma TAG ativa por vez')]
    _sql_constraints = [('occ.veiculo', 'UNIQUE (tag_id)',
                         'Tag já cadastrado')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(string='Placa', size=8, required=True)
    tipo = fields.Selection([('carro', 'Carro'), ('moto', 'Moto')], "Tipo",
                            default='carro', required=True)
    morador_id = fields.Many2one('occ.morador', 'Morador', ondelete="cascade",
                                 required=True)
    tag_id = fields.Many2one('occ.tag', 'TAG', required=True,
                             domain="[('tipo','=',tipo)]")
    status = fields.Selection([('vaga', 'Na vaga'), ('fora', 'Na rua')],
                              "Situação", default='vaga', required=True)
