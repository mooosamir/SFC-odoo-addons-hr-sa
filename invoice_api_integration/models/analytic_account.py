from odoo import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    product_type = fields.Selection(string="",
                                    selection=[
                                        ('1', 'Default Product'),
                                        ('2', 'Ammunition'),
                                        ('4', 'Nafath fees'),
                                        ('5', 'Tickets'),
                                        ('tax', 'TAX'),
                                        ('charge', 'Service Charge'),
                                        ('bank_service', 'Bank Service Charge'),
                                        ('shipping', 'Shipping Fees'),
                                        ('weapon_overage', 'Weapon Overage')
                                    ], required=False, )
    is_ecommerce = fields.Boolean(string="")
