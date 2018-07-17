# -*- coding: utf-8 -*-
{
    'name': "swp_modul",

    'summary': """
        Menambahkan field baru Remote pada timesheet""",

    'description': """
        Modul sederhana menambahkan field Remote pada timeshee
    """,

    'author': "Satiya WaraPutra",
    'website': "satiya-share.blogspot.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','analytic','account','project','hr','hr_timesheet_sheet','hr_timesheet'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/timesheet_remote.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}