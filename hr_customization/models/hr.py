# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError, UserError
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)


class HRPayslip(models.Model):
    _inherit = 'hr.payslip'
    notes = fields.Text()

    def send_payslip(self):
        template = self.env.ref('hr_customization.send_payslip_email_id')
        assert template._name == 'mail.template'

        template_values = {
            'email_to': '${object.email_from|safe}',
            'email_cc': '${object.email_cc|safe}',
            'auto_delete': True,
            'partner_to': False,
            'scheduled_date': False,
        }
        template.write(template_values)

        for rec in self:
            if not rec.employee_id.work_email:
                raise UserError(_("Cannot send email: Employee %s has no email address.") % rec.name)
            with self.env.cr.savepoint():
                force_send = not (self.env.context.get('import_file', False))
                template.with_context(lang=self.env.user.lang).send_mail(rec.id, force_send=force_send,
                                                                         raise_exception=True)
            _logger.info("Payslip email sent  to <%s>", rec.employee_id.work_email)

    def action_payslip_done(self):
        res = super(HRPayslip, self).action_payslip_done()
        for rec in self:
            rec.send_payslip()
        return res


class HREmployee(models.Model):
    _inherit = 'hr.employee'
    secrit_number = fields.Char()


class HRContract(models.Model):
    _inherit = 'hr.contract'
    cla = fields.Selection([
        ('club_emp', 'Club Employees'),
        ('agree', 'Agreement'),
        ('solution_emp', 'Solution Employees')], default='solution_emp', string="Class")

    is_confirm = fields.Boolean()

    @api.onchange('wage', 'cla')
    def _onchange_wage(self):
        if self.cla == 'club_emp':
            if self.wage > 0:
                self.basic = self.wage / 1.4
                self.HRA = self.basic * 0.30
                self.TA = self.basic * 0.1

        elif self.cla == 'agree':
            if self.wage > 0:
                self.basic = self.wage
                self.HRA = 0
                self.TA = 0


        elif self.cla == 'solution_emp':
            if self.wage > 0:
                self.basic = self.wage / 1.35
                self.HRA = self.basic * 0.25
                self.TA = self.basic * 0.1

    def confirm_contract(self):
        for rec in self:
            rec.is_confirm = True

    @api.onchange('state', 'is_confirm')
    def check_contract_confirm(self):
        if self._origin:
            if self.is_confirm == False and self.state == 'open':
                raise ValidationError(_("Firstly Please Confirm Contract"))
            pass


class HRContractExpire(models.Model):
    _name = 'hr.contract.expire'

    def expire_contract(self):
        contracts = self.env['hr.contract'].search([])

        users = self.env['res.users'].search([])
        for c in contracts:
            if c.date_end:
                duration = ((c.date_end - datetime.today().date()).days) + 1
                if duration == 90:
                    for user in users.filtered(
                            lambda u: u.has_group('hr_customization.group_expiration_contract') == True):
                        c.activity_schedule('hr_customization.schdule_activity_expire_id', datetime.today().date(),
                                            user_id=user.id,
                                            summary='Contract will expire in 90 days')
