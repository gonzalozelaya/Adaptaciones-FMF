# -*- coding: utf-8 -*-
{
    'name': "adaptaciones_FMF",

    'summary': """
        Cambios hechos para adaptar al funcionamiento de la empresa""",

    'description': """
        Cambios hechos para adaptar al funcionamiento de la empresa
    """,

    'author': "OutsourceArg",
    'website': "http://www.outsourcearg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','stock','account.move'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
}