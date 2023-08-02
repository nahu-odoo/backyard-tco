from odoo import api, fields, models


class NewModel(models.Model):
    _name = "new.model"

    name = fields.Char()

    @api.model
    def create(self, vals):
        return super().create(vals)

    def generate_data(self):
        data = [{'name': i} for i in range(100)]
        self.create(data)
