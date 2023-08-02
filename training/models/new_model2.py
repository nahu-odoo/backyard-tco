from odoo import api, fields, models

class NewModel2(models.Model):
    _name = "other.model"
    name = fields.Char()

    @api.model_create_multi
    def create(self, vals_list):
        super().create(vals_list)

    def generate_data(self):
        data = [{'name': i} for i in range(100)]
        self.create(data)
