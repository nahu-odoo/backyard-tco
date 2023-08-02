from odoo import api, fields, models

class QtyWiz(models.TransientModel):
    _name = "qty.wizard"

    quantity = fields.Integer()
    order_id = fields.Many2one("sale.order")

    def action_confirm(self):
        self.order_id.order_line.write({"product_uom_qty": self.quantity})
