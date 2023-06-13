from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    rental_ids = fields.One2many("library.rental", "user_id")
