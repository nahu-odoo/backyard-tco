from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_items = fields.Integer("Total Items", compute="_compute_total_items")
    expense_level = fields.Selection(selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], compute="_compute_expense_level")
    customer_phone = fields.Char(related="partner_id.phone")

    @api.depends('order_line.product_uom_qty')
    def _compute_total_items(self):
        for rec in self:
            rec.total_items = sum(rec.order_line.mapped('product_uom_qty'))

    @api.depends('amount_total')
    def _compute_expense_level(self):
        for rec in self:
            if rec.amount_total <= 10:
                rec.expense_level = 'low'
            elif rec.amount_total > 10 and rec.amount_total <= 100:
                rec.expense_level = 'medium'
            elif rec.amount_total > 100:
                rec.expense_level = 'high'

# SHELL STUFF
# env['sale.order'].search([])
# env['sale.order'].search([('amount_total', '>', 500)])
# env['sale.order'].search([]).filtered(lambda x: x.state =='draft')
# env['sale.order'].search([]).partner_id
