# -*- coding: utf-8 -*-
import re
from openerp import models, fields, api
from oc_base.models import oc_models
from oc_base.models import occ_morador
from oc_virdi.models import vd_packs


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
    name = fields.Boolean('Sucesso')
    
