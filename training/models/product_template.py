from odoo import api, fields, models

class ProductProduct(models.Model):
    _inherit = "product.template"

    min_age = fields.Integer("Minimum Age")
