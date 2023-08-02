from odoo import api, models

class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['email'] = vals['name'].replace(' ', '.') + '@odoo.com'
            # vals['email'] = vals['name'].lower().replace(' ', '.') + '@odoo.com'
        return super().create(vals)
