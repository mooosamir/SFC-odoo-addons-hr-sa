# -*- coding: utf-8 -*-
{
    'name': "Payroll Batch Chatter",
    'summary': """
        Payroll Batch Chatter
    """,
    'description': """
        Payroll Batch Chatter
    """,
    'author': "erp-bank",
    'website': "www.erp-bank.com",
    'depends': ['base', 'hr_payroll','utm','portal','mail'],
    'data': [
        'views/hr_payslip_run.xml',
    ],
}