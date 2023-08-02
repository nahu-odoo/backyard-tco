from odoo import api, fields, models
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.email = self.name.replace(' ', '_').lower() + "@odoo.com"

    @api.model
    def create(self, vals):
        raise UserError(vals.items())
        return super().create(vals)

    def write(self, vals):
        raise UserError(vals.items())
        return super().write(vals)
