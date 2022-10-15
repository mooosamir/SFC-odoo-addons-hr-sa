# -*- coding: utf-8 -*-
{
    'name': 'Hr Customization',
    'category': 'Hr Customization',
    'summary': 'Hr Customization',
    'author': "erp-bank",
    'website': "www.erp-bank.com",
    'depends': ['hr', 'hr_holidays','hr_contract','saudi_hr','saudi_hr_payroll','hr_payroll','saudi_hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/hr_view.xml',
        'report/payslip_report.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
