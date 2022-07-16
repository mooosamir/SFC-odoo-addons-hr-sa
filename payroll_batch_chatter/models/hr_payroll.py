from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date, datetime
from dateutil.relativedelta import relativedelta



class HrPayslipRun(models.Model):
    _name='hr.payslip.run'
    _inherit = ['hr.payslip.run','portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Verify'),
        ('first_approve', 'First Approve'),
        ('second_approve', 'Second Approve'),
        ('CEO_approve', 'Third Approve'),
        ('GM_approve', 'Fourth Approve'),
        ('close', 'Done'),
        ('cancel', 'Rejected'),

    ], string='Status', index=True, readonly=True, copy=False, default='draft',tracking=1)

    name = fields.Char(required=True, readonly=True, states={'draft': [('readonly', False)]},tracking=1)

    date_start = fields.Date(string='Date From', required=True, readonly=True,tracking=1,
        states={'draft': [('readonly', False)]}, default=lambda self: fields.Date.to_string(date.today().replace(day=1)))
    date_end = fields.Date(string='Date To', required=True, readonly=True,tracking=1,
        states={'draft': [('readonly', False)]},
        default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()))
    credit_note = fields.Boolean(string='Credit Note', readonly=True,tracking=1,
        states={'draft': [('readonly', False)]},
        help="If its checked, indicates that all payslips generated from here are refund payslips.")

