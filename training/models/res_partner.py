from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    date_of_birth = fields.Date("Date of Birth")
    phone = fields.Char("Phone Number")
