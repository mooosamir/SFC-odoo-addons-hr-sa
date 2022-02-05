# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError



class HrPayslip(models.Model):
    _inherit ='hr.payslip'


    def _get_worked_day_lines(self):
        res=super(HrPayslip, self)._get_worked_day_lines()
        lines={}
        work_entry=self.env.ref('hr_time_off_installment.work_entry_type_leave_pay')
        time_request = self.env['hr.leave'].search(
            [('state', '=', 'validate'), ('employee_id', '=', self.employee_id.id),
             ('date_from','>=',self.date_from),('date_to','<=',self.date_to),
             ('pay_in_advance', '=', 'yes')])

        if sum(time.number_of_days for time in time_request) > 0:
             for line in work_entry:
                if len(res) > 0:
                    if line.id != res[0]['work_entry_type_id']:
                        lines = {
                            'sequence': line.sequence,
                            'work_entry_type_id': line.id,
                            'number_of_days':self._round_days(work_entry,sum(time.number_of_days for time in time_request)),
                            'number_of_hours': 0.0,
                            'amount': 0.0,
                        }
                        res.append(lines)
                else:
                    lines = {
                        'sequence': line.sequence,
                        'work_entry_type_id': line.id,
                        'number_of_days': self._round_days(work_entry,sum(time.number_of_days for time in time_request)),
                        'number_of_hours': 0.0,
                        'amount': 0.0,
                    }
                    res.append(lines)
        return res
