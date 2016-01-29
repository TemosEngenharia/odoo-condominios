# -*- coding: utf-8 -*-
{
    'name': "Controle de Acesso",

    'summary': """
        Aplicativo de controle de acesso de portaria no Odoo""",

    'description': """
        Sistema de Controle de Acesso dos itens:
            - Moradores
            - Vagas
            - Carros
            - Motos
            - TAGs
    """,

    'author': "E2i9",
    'website': "http://www.e2i9.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module
    # /module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '9.0.0.0.1',

    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
             'security/oc_base_security.xml',
             'security/ir.model.access.csv',
             'views/oc_view.xml',
             'views/oc_Cad_view.xml',
             'views/oc_Opr_view.xml',
             'views/oc_Sol_view.xml',
             'views/oc_Hlp_view.xml',
             'views/occ_bloco_view.xml',
             'views/occ_apto_view.xml',
             'views/occ_morador_view.xml',
             'views/occ_veiculo_view.xml',
             'views/occ_vaga_carro_view.xml',
             'views/occ_vaga_moto_view.xml',
             'views/occ_tag_view.xml',
             'views/occ_visitante_view.xml',
             'views/occ_empresa_view.xml',
             'views/occ_funcionario_view.xml',
    ],
}
