
{
    'name': "Account Confirmation Step",
    'summary': """Account Confirmation Step""",
    'description': """
       Account Confirmation Step
    """,
    'author': "erp-bank",
    'category': 'Generic Modules/Account',
    'version': '1.0',
    'depends': [
        'base','account'
    ],
    'data': [
        'security/res_group.xml',
        'views/res_congfig_settings.xml',
        'views/account_move_view.xml',
        'views/account_payment_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
