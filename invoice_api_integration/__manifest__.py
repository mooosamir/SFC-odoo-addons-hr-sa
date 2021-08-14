# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Invoices Api Integration",
    "version": "14",
    "category": "Extra Tools",
    "description": """
Manage ecommerce api
==================================
""",
    "author": "Ahmed",
    "depends": [
        'base',
        'web',
        'product',
        'account',
        'account_accountant',
        'analytic',
    ],
    "data": [
        'views/account_tax.xml',
        'views/account_journal.xml',
        'views/res_partner_view.xml',
        'views/product_template_view.xml',
        'views/account_analytic.xml',
        'views/account_invoice.xml',
        'views/product_data_view.xml',
    ],
    "auto_install": False,
    "installable": True,
}
