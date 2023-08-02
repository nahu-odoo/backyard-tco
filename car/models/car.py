from odoo import models, fields

class Car(models.Model):
    _name = "car.car"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    production_date = fields.Date()
    brand = fields.Char()
    miles = fields.Integer()
    picture = fields.Binary()
    price = fields.Float()
    user_id = fields.Many2one('res.partner')

    def add_miles(self):
        self.miles += 1000
