# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError

class ResCompany(models.Model):
    _inherit = "res.company"
    account_limit_amount=fields.Float()
    use_account_limit_amount = fields.Boolean(
        string='Limit Amount',config_parameter='account_confirmation_step.use_account_limit_amount')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    account_limit_amount=fields.Float(related='company_id.account_limit_amount',readonly=False)
    use_account_limit_amount = fields.Boolean(related='company_id.use_account_limit_amount',readonly=False,
        string='Limit Amount',config_parameter='account_confirmation_step.use_account_limit_amount')


