from datetime import datetime
from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare
class WizardBankFile(models.TransientModel):
   _name = "wizard.bank.file"
   date_from = fields.Date(required=True)
   date_to = fields.Date(required=True)
   state=fields.Selection([
      ('verify','Waiting'),
      ('done','Done'),
   ],default='verify',required=True)

   @api.constrains('date_from','date_to')
   def check_date(self):
      if self.date_from != False and self.date_to != False:
         if self.date_from > self.date_to:
              raise ValidationError(_("Date From should not be greater than Date To."))

   def print_excel(self):
      active_record = self.env.context.get('active_ids', [])
      record = self.env['sale.order'].browse(active_record)

      data = {
         'ids': self.ids,
         'model': self._name,
         'record': record.id,
      }
      action = self.env.ref('bank_salary_report.bank_salary_report_excel_id').report_action(self, data=data)
      action.update({'close_on_report_download': True})
      return action



