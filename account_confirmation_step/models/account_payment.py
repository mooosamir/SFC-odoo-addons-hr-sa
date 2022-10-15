# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta


class AccountPayment(models.Model):
    _inherit = "account.payment"
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

    def action_submitted(self):
        for rec in self:
            rec.write({'state': 'submitted'})

    def action_validated(self):
        for rec in self:
            rec.write({'state': 'validated'})

    def action_GM_approve(self):
        for rec in self:
            rec.write({'state': 'gm_approved'})

    def action_cancel(self):
        super(AccountPayment, self).action_cancel()
        self.write({"state":"cancel"})

    def action_post(self):
        super(AccountPayment, self).action_post()
        self.write({"state":"posted"})

    def action_draft(self):
        super(AccountPayment, self).action_post()
        self.write({"state":"draft"})

    def action_CEO_approve(self):
        for rec in self:
            # if rec.amount < rec.company_id.account_limit_amount:
            #     # rec.action_post()
            #      rec.write({"state":"posted"})
            # elif rec.amount > rec.company_id.account_limit_amount:
            #   rec.write({'state' : 'ceo_approved'})

            if rec.amount < rec.company_id.sudo().po_double_validation_amount:
                rec.write({"state": "posted"})
            elif rec.amount >= rec.company_id.sudo().po_double_validation_amount:
                rec.write({'state': 'ceo_approved'})
