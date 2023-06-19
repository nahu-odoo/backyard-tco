import datetime
from dateutil.relativedelta import relativedelta
from odoo.tests import tagged, common

@tagged('rental', 'post_install', '-at_install')
class TestRental(common.TransactionCase):
    def setUp(self):
        super().setUp()

    def test_rental_create(self):
        today = datetime.datetime.today()
        book = self.env['library.book'].create({'name': 'Test Book'})
        user = self.env['res.partner'].create({'name': 'Test User'})
        rental = self.env['library.rental'].create({'book': book.id, 'user_id': user.id})

        self.assertEqual(rental.date, today.date())
        self.assertEqual(rental.due_date, today.date() + relativedelta(months=1))

        rental.due_date = today.date() - relativedelta(days=2)
        self.assertEqual(rental.overdue_fine, 20)
