# -*- coding: utf-8 -*-
from openerp import models, fields


class OccBloco(models.Model):
    _name = 'occ.bloco'
    _description = 'Detalhes dos Blocos'
    _order = 'name'
    _table = 'occ_bloco'
    _sql_constraints = [('occ.bloco', 'UNIQUE (name)',
                         'Os nomes dos blocos devem ser únicos')]
    active = fields.Boolean('Ativo', default=True)
    name = fields.Char('Bloco', size=4, required=True)
    apto_ids = fields.One2many('occ.apto', 'bloco_id',
                               'Apartamentos neste bloco')
    morador_ids = fields.One2many('occ.morador', 'bloco_id',
                                  'Moradores neste bloco')
    vaga_carro_ids = fields.One2many('occ.vaga.carro', 'bloco_id',
                                     'Vagas para Carros neste bloco')
    vaga_moto_ids = fields.One2many('occ.vaga.moto', 'bloco_id',
                                    'Vagas para Motos neste bloco')
