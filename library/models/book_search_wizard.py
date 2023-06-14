from odoo import fields, models
from odoo.exceptions import UserError

class SearchWizard(models.TransientModel):
    _name = "book.search.wizard"

    book_name = fields.Char()

    def action_search(self):
        book = self.env['library.book'].search([('name', 'ilike', self.book_name)])
        if not book:
            raise UserError("No book with this name is found!")

        action = {
            "name": "Books",
            "type": "ir.actions.act_window",
            "res_model": "library.book",
            "views": [(False, "form")],
        }
        if len(book) == 1:
            action['res_id'] = book.id
        else:  # len(book) == 1
            action['domain'] = [('id', 'in', book.ids)]
            action["views"] = [(False, "tree")] + action["views"]

        return action
