# -*- coding: utf-8 -*-
import re
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from . import cpf


class OccVisitante(models.Model):
    _name = 'occ.visitante'
    _description = 'Detalhes dos Moradores'
    _order = 'name'
    _table = 'occ_visitante'
    _sql_constraints = [
        ('occ.visitante', 'unique (cpf)',
         'Já existe um visitante cadastrado com este CPF!')
    ]

    active = fields.Boolean('Ativo', default=True)
    name = fields.Char('Visitante', size=45, required=True)
    image = fields.Binary('Foto')
    rg = fields.Char('RG', size=15, required=True)
    cpf = fields.Char('CPF', size=15, required=True)
    fone = fields.Char('Telefone', size=18)
    celular = fields.Char('Celular', size=18)

    @api.onchange('cpf')
    def _onchange_cpf(self):
        cpf = None
        if self.cpf:
            val = re.sub('[^0-9]', '', self.cpf)
            if len(val) == 11:
                cpf = "%s.%s.%s-%s" % (
                    val[0:3], val[3:6], val[6:9], val[9:11])
                self.cpf = cpf

    @api.onchange('celular')
    def _onchange_celular(self):
        celular = None
        if self.celular:
            val = re.sub('[^0-9]', '', self.celular)
            if len(val) == 11:
                celular = "%s-%s.%s.%s" % (val[0:2], val[2:5], val[5:8],
                                           val[8:11])
            self.celular = celular

    @api.onchange('fone')
    def _onchange_fone(self):
        fone = None
        if self.fone:
            val = re.sub('[^0-9]', '', self.fone)
            if len(val) == 10:
                fone = "%s-%s.%s" % (val[0:2], val[2:6], val[6:10])

            self.fone = fone

    @api.one
    @api.constrains('cpf')
    def _check_cpf(self):
        result = True
        if self.cpf:
            if not cpf.validate_cpf(self.cpf):
                result = False
                document = 'CPF'
            if not result:
                raise ValidationError("{} Inválido!".format(document))
