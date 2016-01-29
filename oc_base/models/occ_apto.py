# -*- coding: utf-8 -*-
from openerp import models, fields


class OccApto(models.Model):
    _name = 'occ.apto'
    _description = 'Detalhes dos Apartamentos'
    _order = 'name'
    _table = 'occ_apto'
    _sql_constraints = [('occ.apto', 'UNIQUE (name)',
                         'Os nomes dos apartamentos devem ser únicos')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char('Apartamento', size=4, required=True)
    numero = fields.Char('Número', size=4, required=True)
    morador_ids = fields.One2many('occ.morador', 'apto_id',
                                  'Moradores neste Apartamento')
    bloco_id = fields.Many2one('occ.bloco', 'Bloco',
                               ondelete="cascade", required=True)
    vaga_carro_id = fields.Many2one('occ.vaga.carro', 'Vaga Carro',
                                    domain="[('bloco_id','=',bloco_id)]")
    vaga_moto_id = fields.Many2one('occ.vaga.moto', 'Vaga Moto',
                                   domain="[('bloco_id','=',bloco_id)]")
