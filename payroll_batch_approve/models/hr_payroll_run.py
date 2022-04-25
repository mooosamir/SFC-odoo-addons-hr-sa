# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class HrPayrollRun(models.Model):
    _inherit = "hr.payslip.run"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Verify'),
        ('first_approve', 'First Approve'),
        ('second_approve', 'Second Approve'),
        ('close', 'Done'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')


    def action_first_approve(self):
        for rec in self:
            rec.write({'state' : 'first_approve'})

    def action_second_approve(self):
        for rec in self:
            rec.write({'state' : 'second_approve'})





