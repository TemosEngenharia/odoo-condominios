# -*- coding: utf-8 -*-
{
    'name': "Gestão dos módulos Virdi pela rede",

    'summary': """
        Acesso aos módulos de controle de acesso da Virdi""",

    'description': """
        Módulos para controle das unidades AC-1000, AC-2500 da Virdi
    """,

    'author': "E2i9",
    'website': "http://www.e2i9.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module
    # /module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '9.0.1.0.0',

    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'oc_base', ],

    # always loaded
    'data': [
            'security/oc_virdi_security.xml',
            'security/ir.model.access.csv',
            'views/occ_controle_acesso.xml',
            'views/occ_virdi.xml',
    ],
}
