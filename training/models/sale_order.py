from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def get_amount_per_partner_search(self, customers):
        # use search to get the amount per partner
        data = {}
        for customer in customers:
            sale_orders = self.search([('partner_id', '=', customer.id)])
            data[customer.id] = sum(sale_orders.mapped('amount_total'))
        return data

    @api.model
    def get_amount_per_partner_read_group(self, customers):
        # using read_group to get the amount per partner
        data = {}
        sale_order_groups = self.read_group([('partner_id', 'in', customers.ids)], ["amount_total"], ["partner_id"])
        for group in sale_order_groups:
            data[group['partner_id'][0]] = group['amount_total']
        return data

    def get_highest_sale(self):
        return self.env['sale.order'].search([], order="amount_total DESC", limit=1)

    @api.model
    def search_and_sort_amount(self):
        return self.search([]).sorted(lambda x: x.amount_total, reverse=True)[0].amount_total

    @api.model
    def search_sorted(self):
        return self.search([], order="amount_total DESC", limit=1).amount_total
