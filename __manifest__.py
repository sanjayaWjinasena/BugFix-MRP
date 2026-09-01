# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : MRP',
    'version': '17.0.0.0.15',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.15: wire 3 base.automation stubs + port 2 backing server actions.
    #   * data/server_actions.xml grows from 2 to 4 records:
    #     1155 Update Original MO in MO (247b, on mrp.production)
    #     1738 SRM Auto Populate Report Type in Production Order (209b,
    #          on mrp.production; runtime lookup on x_sales_report_type)
    #   * data/automations.xml: all 3 TODO comments replaced by
    #     <field name="action_server_ids" eval="[(6, 0, [ref('server_action_NNNN_...')])]"/>
    #     Trigger semantics preserved.
    #   * 3 base.automation records now actually invoke their server
    #     actions on trigger; previously they were silent no-ops.
    # Mirrors BugFix-Stock v0.0.15 + BugFix-Accounting v0.0.47 pattern.
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