# -*- coding: utf-8 -*-
{
    'name': "Cadastro Controle de Acesso",

    'summary': """
        Módulo para realizar o cadastro dos veículos, vagas, moradores,
        apartamentos, blocos e TAGs""",

    'description': """
        Módulo do Sistema de Controle de Acesso para realizar o cadastro dos itens:
            - Blocos
            - Apartamentos
            - Vagas para carro
            - Vagas para motos
            - Moradores
            - Carros
            - Motos
            - TAGs
    """,

    'author': "E2i9",
    'website': "http://www.e2i9.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '9.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'oc-base'],
    'auto_install': False,

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/occ_bloco_views.xml',
        'views/occ_apto_views.xml',
        'views/occ_pessoas_views.xml',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo.xml',
    #],
}