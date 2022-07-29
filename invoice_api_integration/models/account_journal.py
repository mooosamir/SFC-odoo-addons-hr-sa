from odoo import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.journal'

    is_ecommerce = fields.Boolean(string="")
    is_ecommerce_default_payment_account = fields.Boolean(string="Ecommerce Default Payment Account")
