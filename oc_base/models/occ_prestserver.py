# -*- coding: utf-8 -*-
import re
from openerp import models, fields, api
from openerp.exceptions import ValidationError
from . import cpf


class OccEmpresa(models.Model):
    _name = 'occ.empresa'
    _description = u'Detalhes das Empresas Prestadoras de Serviço'
    _order = 'name'
    _rec_name = 'name'
    _table = 'occ_empresa'

    active = fields.Boolean('Ativo', default=True)
    name = fields.Char(u'Empresa', size=45, required=True)
    contato = fields.Char(u'Contato na empresa', size=45)
    fone = fields.Char(u'Telefone comercial fixo', size=18, required=True)
    celular = fields.Char(u'Celular comercial', size=18)
    funcionario_ids = fields.One2many('occ.funcionario', 'empresa_id',
                                      u'Funcionários cadastrados nesta empresa'
                                      )


class OccFuncionario(models.Model):
    _name = 'occ.funcionario'
    _description = u'Detalhes dos Prestadores de Serviço'
    _order = 'name'
    _table = 'occ_funcionario'
    _sql_constraints = [
        ('occ.funcionario', 'unique (cpf)',
         u'Já existe um prestador cadastrado com este CPF!')
    ]

    active = fields.Boolean('Ativo', default=True)
    name = fields.Char('Prestador', size=45, required=True)
    image = fields.Binary('Foto')
    rg = fields.Char('RG', size=15, required=True)
    cpf = fields.Char('CPF', size=15, required=True)
    fone = fields.Char('Telefone', size=18)
    celular = fields.Char('Celular', size=18)
    empresa_id = fields.Many2one('occ.empresa', 'Empresa',
                                 ondelete="cascade", required=True)

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
                raise ValidationError(u"{} Inválido!".format(document))
