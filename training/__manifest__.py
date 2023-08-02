# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Training',
    'version': '1.0',
    'summary': 'Training',
    'description': """
        Training
    """,
    'depends': ['base', 'sale_management', 'contacts'],
    'data': [
        "views/res_partner.xml",
        "views/sale_order.xml",
        "security/ir.model.access.csv",
        "views/qty_wizard.xml",
    ],
    'license': 'LGPL-3',
}
