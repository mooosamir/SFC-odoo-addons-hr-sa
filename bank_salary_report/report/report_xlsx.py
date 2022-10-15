# -*- encoding: utf-8 -*-
from datetime import datetime, timedelta
from odoo.http import request
from odoo import api, fields, models, _
from io import BytesIO
from calendar import monthrange


class BankFileReportXLS(models.AbstractModel):
    _name = 'report.bank_salary_report.bank_salary_report_excel'
    _inherit = 'report.report_xlsx.abstract'

    def number_of_days_in_month(self, year, month):
        return monthrange(year, month)[1]

    def generate_xlsx_report(self, workbook, data, lines):
        wizard_record = request.env['wizard.bank.file'].search([])[-1]
        header_title_format = workbook.add_format({
            'border': 2,
            'border_color': 'black',
            'align': 'center',
            'font_color': '#0b034d;',
            'bold': True,
            'valign': 'vcenter',
            'fg_color': 'white'})
        header_title_format.set_text_wrap()
        header_title_format.set_font_size(18)
        header_title_format1 = workbook.add_format({
            'border': 2,
            'border_color': 'black',
            'align': 'center',
            'font_color': '#0b034d;',
            'bold': True,
            'valign': 'vcenter',
            'fg_color': 'white'})
        header_title_format1.set_text_wrap()
        header_title_format1.set_font_size(25)

        header2_format = workbook.add_format({
            'border': 2,
            'border_color': 'black',
            'align': 'center',
            'font_color': 'white',
            'bold': True,
            'valign': 'vcenter',
            'fg_color': '#336699'})
        header2_format.set_text_wrap()
        header2_format.set_font_size(12)

        header3_format = workbook.add_format({
            'border': 2,
            'border_color': 'black',
            'align': 'center',
            'font_color': 'black',
            'bold': False,
            'valign': 'vcenter',
            'fg_color': '#FFFFFF'})
        header3_format.set_text_wrap()
        header3_format.set_font_size(12)

        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 15)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 30)
        worksheet.set_column('G:G', 30)
        worksheet.set_column('F:F', 20)
        worksheet.set_column('H:H', 15)
        worksheet.set_column('I:I', 15)
        worksheet.set_column('J:J', 15)
        worksheet.set_column('K:K', 20)
        worksheet.set_column('L:L', 25)
        worksheet.set_column('M:M', 15)
        worksheet.set_column('N:N', 15)
        worksheet.set_column('O:O', 25)
        worksheet.set_column('P:P', 15)
        worksheet.set_column('Q:Q', 15)
        worksheet.set_column('R:R', 15)
        worksheet.set_column('S:S', 15)
        worksheet.set_column('T:T', 15)
        worksheet.set_column('U:U', 15)
        worksheet.set_column('V:V', 15)
        worksheet.set_column('W:W', 15)
        worksheet.set_row(0, 35)

        worksheet.write('A1', 'Bank', header2_format)
        worksheet.write('B1', 'Account Number', header2_format)
        worksheet.write('C1', 'Total Salary', header2_format)
        worksheet.write('D1', 'Transaction Reference', header2_format)
        worksheet.write('E1', 'Employee Name', header2_format)
        worksheet.write('F1', 'National ID/Iqama ID', header2_format)
        worksheet.write('G1', 'Employee Address', header2_format)
        worksheet.write('H1', 'Basic Salary', header2_format)
        worksheet.write('I1', 'Housing Allowance', header2_format)
        worksheet.write('J1', 'Other Earnings', header2_format)
        worksheet.write('K1', 'Deductions', header2_format)


        for wizard in wizard_record:
            col = 0
            row = 1
            ser = 0
            payslips_data = """SELECT pay.id as payslip , pay.employee_id as employee , pay.name as ref,
            SUM(CASE WHEN pl.rule_type ='BASIC' THEN pl.amount ELSE 0 END) as basic
            ,SUM(CASE WHEN pl.rule_type  ='Housing' THEN pl.amount ELSE 0 END) as housing,
            SUM(CASE WHEN pl.rule_type  ='Other' THEN pl.amount ELSE 0 END) as other_earnings,
            SUM(CASE WHEN pl.rule_type  ='Deductions' THEN pl.amount ELSE 0 END) as deductions
            FROM hr_payslip pay
            INNER JOIN hr_payslip_line pl ON pl.slip_id = pay.id
            WHERE pay.date_from >= '""" + str(wizard.date_from) + """' AND pay.date_to <= '""" + str(
                wizard.date_to) +"""' AND pay.state = '""" +str(wizard.state) + """'"""+""" GROUP BY payslip , employee , ref
                ORDER BY payslip"""
            cr = self._cr
            cr.execute(payslips_data)
            payslips = cr.dictfetchall()
            for payslip in payslips:
                ser += 1
                employee = self.env['hr.employee'].browse(payslip['employee'] or False)
                worksheet.write(row, col,employee.bank_account_id.bank_id.name or '', header3_format)
                worksheet.write(row, col + 1, employee.bank_account_id.acc_number or '', header3_format)
                worksheet.write(row, col + 2,(payslip['basic'] or 0.0)+(payslip['housing'] or 0.0)+(payslip['other_earnings'] or 0.0)+(payslip['deductions'] or 0.0), header3_format)
                worksheet.write(row, col + 3, '', header3_format)
                worksheet.write(row, col + 4,((employee.name or '') +' '+(employee.middle_name  or '')+' '+ (employee.last_name or '')) or '', header3_format)
                worksheet.write(row, col + 5, employee.iqama_number or employee.identification_id or '', header3_format)
                worksheet.write(row, col + 6, employee.address_home_id.name or '', header3_format)
                worksheet.write(row, col + 7, payslip['basic'] or 0.0, header3_format)
                worksheet.write(row, col + 8, payslip['housing'] or 0.0, header3_format)
                worksheet.write(row, col + 9, payslip['other_earnings'] or 0.0, header3_format)
                worksheet.write(row, col + 10, payslip['deductions'] or 0.0, header3_format)
                row += 1

        return
