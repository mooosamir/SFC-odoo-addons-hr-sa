# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class AccountPayment(models.Model):
    _inherit = "account.payment"
    def action_submitted(self):
        for rec in self:
            rec.write({'state' : 'submitted'})

    def action_validated(self):
        for rec in self:
            rec.write({'state' : 'validated'})


    def action_GM_approve(self):
        for rec in self:
                rec.write({'state' : 'gm_approved'})

    def action_CEO_approve(self):
        for rec in self:
            if rec.amount < rec.company_id.account_limit_amount:
                rec.action_post()
            elif rec.amount > rec.company_id.account_limit_amount:
                rec.write({'state' : 'ceo_approved'})


