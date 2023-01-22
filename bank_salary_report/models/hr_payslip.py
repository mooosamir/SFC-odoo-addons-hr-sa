# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError

class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'
    rule_type=fields.Selection([
        ('BASIC','BASIC'),
        ('Housing','Housing Allowance'),
        ('Other','Other Earnings'),
        ('Deductions','Deductions'),
    ])

class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'
    rule_type=fields.Selection([
        ('BASIC','BASIC'),
        ('Housing','Housing Allowance'),
        ('Other','Other Earnings'),
        ('Deductions','Deductions'),
    ],related='salary_rule_id.rule_type',store=True)

