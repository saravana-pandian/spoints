# -*- coding: utf-8 -*-
{
    'name': "spoints",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "saravana",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website', 'mail',],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    'demo': [
        'demo/demo.xml',
    ],
}