# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Training',
    'version': '1.0',
    'summary': 'Training',
    'description': """
        Training
    """,
    'depends': ['base', 'contacts', 'sale_management'],
    'data': [
        "views/res_partner.xml",
        "views/report_res_partner.xml",
        "views/report_sale_order.xml",
    ],
    'license': 'LGPL-3',
}
