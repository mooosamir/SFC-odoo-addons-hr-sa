# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bank Salary Report',
    'version': '13.0.0.0',
    'category': 'payroll',
    'summary': 'Bank Salary Report',
    "description": """
            Bank Salary Report
           """,
    'author': "erp-bank",
    'website': "www.erp-bank.com",
    'depends': ['base','report_xlsx','hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizard/wizard_bank_file_view.xml',
        'report/report.xml',
        'views/hr_salary_rule_view.xml',
    ],

    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

