# -*- coding: utf-8 -*-

{
    'name': 'website_new',
    'version': '15',
    'summary': 'Enquiry form',
    'author': 'PMCL',
    'depends': ['base','website','crm',],
    'category': 'website',
    'data': [
        'security/ir.model.access.csv',
        'views/website_new.xml',
        'views/website_label_crm.xml',
    ],
    # 'assets': {
        # 'web.assets_backend': [
        #     '/website_new/static/src/js/website_cont.js'
        # ],
    'installable': True,
    'application': False,
    'auto_install': False,
    # },
}

