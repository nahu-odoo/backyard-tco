# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Training',
    'version': '1.0',
    'summary': 'Training',
    'description': """
        Training
    """,
    'depends': ['base', 'sale', 'portal', 'website'],
    'data': [
        "views/template.xml",
        "views/portal_sale_template.xml",
        "views/sample_template.xml",
        "views/sale.xml",
    ],
    'license': 'LGPL-3',
}
