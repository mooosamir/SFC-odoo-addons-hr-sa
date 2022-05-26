# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta

class HrPayroll(models.Model):
    _inherit = "hr.payslip"
    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Waiting'),
        ('first_approve', 'First Approve'),
        ('second_approve', 'Second Approve'),
        ('CEO_approve', 'Third Approve'),
        ('GM_approve', 'Fourth Approve'),
        ('done', 'Done'),
        ('cancel', 'Rejected'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft',
        help="""* When the payslip is created the status is \'Draft\'
                \n* If the payslip is under verification, the status is \'Waiting\'.
                \n* If the payslip is confirmed then status is set to \'Done\'.
                \n* When user cancel payslip the status is \'Rejected\'.""")

    def action_first_approve(self):
        for rec in self:
            rec.write({'state' : 'first_approve'})

    def action_second_approve(self):
        for rec in self:
            rec.write({'state' : 'second_approve'})



    def action_CEO_approve(self):
        for rec in self:
            rec.write({'state' : 'CEO_approve'})

    def action_GM_approve(self):
        for rec in self:
            rec.write({'state' : 'GM_approve'})

    def action_payslip_cancel(self):
        if self.filtered(lambda slip: slip.state == 'done'):
            raise UserError(_("Cannot cancel a payslip that is done."))
        self.write({'state': 'cancel'})
        if self.mapped('payslip_run_id').filtered(lambda slip: slip.state == 'done'):
            raise UserError(_("Cannot cancel a batch that is done."))
        self.mapped('payslip_run_id').write({'state':'cancel'})





class HrPayrollRun(models.Model):
    _inherit = "hr.payslip.run"

    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Verify'),
        ('first_approve', 'First Approve'),
        ('second_approve', 'Second Approve'),
        ('CEO_approve', 'Third Approve'),
        ('GM_approve', 'Fourth Approve'),
        ('close', 'Done'),
        ('cancel', 'Rejected'),

    ], string='Status', index=True, readonly=True, copy=False, default='draft')


    def action_first_approve(self):
        for rec in self:
            for payslip in self.slip_ids:
                payslip.action_first_approve()
            rec.write({'state' : 'first_approve'})

    def action_second_approve(self):
        for rec in self:
            for payslip in self.slip_ids:
                payslip.action_second_approve()
            rec.write({'state' : 'second_approve'})



    def action_CEO_approve(self):
        for rec in self:
            for payslip in self.slip_ids:
                payslip.action_CEO_approve()

            rec.write({'state' : 'CEO_approve'})

    def action_GM_approve(self):
        for rec in self:
            for payslip in self.slip_ids:
                payslip.action_GM_approve()
            rec.write({'state' : 'GM_approve'})

    def action_payslip_cancel(self):
        if self.filtered(lambda slip: slip.state == 'done'):
            raise UserError(_("Cannot cancel a payslip that is done."))
        self.write({'state': 'cancel'})
        for payslip in self.slip_ids:
            if payslip.filtered(lambda slip: slip.state == 'done'):
                raise UserError(_("Cannot cancel a payslip that is done."))
            payslip.action_payslip_cancel()

    def action_draft(self):
        res=super(HrPayrollRun, self).action_draft()
        for payslip in self.slip_ids:
            payslip.action_payslip_draft()

        return res








