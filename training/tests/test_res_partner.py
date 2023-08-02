from odoo.tests import tagged, common

@tagged('partner', 'post_install', '-at_install')
class TestPartner(common.TransactionCase):
    def setUp(self):
        super().setUp()

    def test_email_change(self):
        new_contact = self.env['res.partner'].create({"name": "John Doe"})
        self.assertEqual(new_contact.email, "john.doe@odoo.com")
