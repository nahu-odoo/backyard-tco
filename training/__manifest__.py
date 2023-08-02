# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Training',
    'version': '1.0',
    'summary': 'Training',
    'description': """
        Training
    """,
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "data/data.xml",
    ],
    'license': 'LGPL-3',
}
