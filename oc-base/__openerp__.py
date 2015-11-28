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
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '9.0.0.0.1',
    
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/oc_views.xml',
        'views/oc_Adm_views.xml',
        'views/oc_Opr_views.xml',
        'views/oc_Hlp_views.xml',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo.xml',
    #],
}