from odoo import api, fields, models
from odoo.exceptions import UserError

class Sale(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        if self.amount_total < 1000:
            raise UserError("Amount is not enough")
        super().action_confirm()

    def set_qty(self):
        return {
            'name': 'Set Quantity',
            'type': 'ir.actions.act_window',
            'res_model': 'qty.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id}
        }
