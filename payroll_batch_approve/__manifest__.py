# -*- coding: utf-8 -*-
# Part of odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "HR Payroll Batch Approve",
    'summary': """HR Payroll Batch Approve""",
    'description': """
       HR Payroll Batch Approve
    """,
    'author': "erp-bank",
    'category': 'Generic Modules/Human Resources',
    'version': '1.0',
    'depends': [
        'base','hr','hr_payroll','hr_payroll_account'
    ],
    'data': [
        'security/res_group.xml',
        'views/hr_payroll_batch_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
