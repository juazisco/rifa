# -*- coding: utf-8 -*-
{
    'name': "Gestor de Rifas",

    'summary': """
        Aplicación simple para gestioanr Rifas""",

    'description': """
        Aplicación simple para gestioanr Rifas
    """,

    'author': "Juazisco",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts'],

    # always loaded
    'data': [
        'security/res.groups.xml',
        'security/ir.model.access.csv',
        #'security/ir.rule.xml',
        'views/views.xml',
        'data/rifa_sequence.xml',
        'views/templates_email.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
