# -*- coding: utf-8 -*-
{
    'name': 'BugFix - MRP',
    'version': '17.0.0.0.12',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    'depends': ['base_setup', 'mrp'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_material_request_m_studio_ported.xml',
        'views/x_material_request_m_stage_studio_ported.xml',
        'views/x_material_request_m_tag_studio_ported.xml',
        'views/mrp_production_studio_ported.xml',
        'views/mrp_workcenter_studio_ported.xml',
        'views/mrp_workorder_studio_ported.xml',
        'views/mrp_bom_studio_ported.xml',
        'views/mrp_eco_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}