# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta


class AccountMove(models.Model):
    _inherit = "account.move"
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('submitted', 'submitted'),
        ('validated', 'Validated'),
        ('gm_approved', 'GM Approved'),
        ('ceo_approved', 'CEO Approved'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True,
        default='draft')
    state_a = fields.Selection(related='state', tracking=False)

    def action_submitted(self):
        for rec in self:
            rec.write({'state': 'submitted'})

    def action_validated(self):
        for rec in self:
            rec.write({'state': 'validated'})

    def action_GM_approve(self):
        for rec in self:
            rec.write({'state': 'gm_approved'})

    def action_CEO_approve(self):

        for rec in self:
            #     if rec.company_id.use_account_limit_amount:
            #         if rec.amount_total < rec.company_id.account_limit_amount:
            #             rec.action_post()
            #         elif rec.amount_total >= rec.company_id.account_limit_amount:
            #             rec.write({'state' : 'ceo_approved'})
            #     else:
            #         rec.action_post()
            if rec.company_id.use_account_limit_amount:
                if rec.amount_total < rec.company_id.sudo().account_limit_amount:
                    rec.write({"state": "posted"})
                elif rec.amount_total >= rec.company_id.sudo().account_limit_amount:
                    rec.write({'state': 'ceo_approved'})
