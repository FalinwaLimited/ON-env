# -*- coding: utf-8 -*-
{
    "name": "Expense Mod for ONG",
    "version": "12.0.0.0.1",
    'author': 'Falinwa Limited',
    'website': 'https://falinwa.com',
    'category': 'Human Resource',
    'summary': 'ONG Expense Modification',
    "description": """
        Modify falinwa expense.
        1. Real currency visible on expense tree view.
        2. Fill in amount currency with real amount.

    """,
    "depends": [
        'fal_hr_expense',
    ],
    'data': [
        'views/hr_expense_inherit_view.xml',
    ],
    'css': [],
    'js': [],
    'installable': True,
    'active': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
