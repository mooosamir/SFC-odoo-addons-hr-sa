# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, UserError


class HRPayslip(models.Model):
    _inherit = 'hr.payslip'
    notes=fields.Text()
class HREmployee(models.Model):
    _inherit = 'hr.employee'
    secrit_number=fields.Char()
class HRContract(models.Model):
    _inherit = 'hr.contract'
    cla=fields.Selection([
        ('club_emp','Club Employees'),
        ('solution_emp','Solution Employees')],default='solution_emp',string="Class")

    is_confirm=fields.Boolean()


    @api.onchange('wage','cla')
    def _onchange_wage(self):
        if self.cla == 'club_emp':
           if self.wage > 0:
                self.basic = self.wage / 1.4
                self.HRA = self.basic * 0.30
                self.TA = self.basic * 0.1

        elif self.cla == 'solution_emp':
           if self.wage > 0:
                self.basic = self.wage / 1.35
                self.HRA = self.basic * 0.25
                self.TA = self.basic * 0.1

    def confirm_contract(self):
        for rec in self:
            rec.is_confirm =True


    @api.onchange('state','is_confirm')
    def check_contract_confirm(self):
        if self._origin:
            if self.is_confirm == False and self.state =='open':
                raise ValidationError(_("Firstly Please Confirm Contract"))
            pass


