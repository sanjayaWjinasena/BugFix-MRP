# -*- coding: utf-8 -*-
{
    'name': 'BugFix - MRP',
    'version': '17.0.0.0.13',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.13: added Jinasena_Masterdata_Reporting - owns x_sales_report_type
    # which our mrp.production Many2one targets. Sentinel Python class
    # for x_sales_report_type removed in favor of the consolidated
    # masterdata module.
    'depends': ['base_setup', 'mrp', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}