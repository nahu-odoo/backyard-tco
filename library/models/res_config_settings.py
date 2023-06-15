from odoo import fields, models

class Settings(models.TransientModel):
    _inherit = "res.config.settings"

    default_penalty = fields.Float(default_model="library.rental")
