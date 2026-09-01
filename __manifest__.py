# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : MRP',
    'version': '17.0.0.0.18',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.18: bulk of small Studio inherits on standard mrp.* models.
    # See views/mrp_studio_ported.xml. 5 views ported byte-verbatim:
    #   * 2390 mrp.production.tree                 (486b)
    #   * 5503 mrp.workcenter.productivity.tree    (277b)
    #   * 3151 mrp.workcenter.tree                 (620b)
    #   * 5062 mrp.eco.view.tree                   (278b)
    #   * 3953 mrp.workorder.view.form (tablet)    (642b)
    # 0 hardcoded action refs, 0 undeclared modifier fields, 0 missing
    # field refs on repair-test-101 after porting x_studio_item_approved
    # boolean on mrp.eco (models/mrp_eco.py). New deps: mrp_plm (5062
    # inherit target) + mrp_workorder (3953 inherit target). Both already
    # installed on repair-test-101 and Clear-DB.
    # Deferred: 4830 mrp.eco form (1634b) - 3 missing fields plus 10
    # undeclared modifier refs need sentinel injection; batched later.
    # v0.0.17: first view-port wave - 4 primary Default views for
    # x_material_request_m. See views/x_material_request_m_studio_ported.xml.
    #   * 8744 tree   (456b)
    #   * 8745 form   (2026b) - oe_chatter stripped (model lacks mail.thread)
    #   * 8746 search (1016b)
    #   * 8749 kanban (2928b)
    # 0 hardcoded action refs, 0 undeclared modifier fields, 0 missing
    # field refs on repair-test-101. x_material_request_m_line_ids_af086
    # O2M (referenced by 8745 form) resolves via v0.0.16 field port.
    # v0.0.16: port x_material_request_m_line_af405 custom model (3 fields)
    # and the O2M navigation from x_material_request_m to it.
    #   * models/x_material_request_m_line_af405.py - new model, 3
    #     Studio x_* fields (x_name, x_studio_sequence, and parent
    #     M2O x_material_request_m_id). 0 rows on Clear-DB.
    #   * models/x_material_request_m.py - x_material_request_m_line_ids_af086
    #     TODO comment replaced with real One2many declaration
    #     targeting the new model via x_material_request_m_id inverse.
    #   * security/ir_model_pins.xml + ir.model.access.csv: pin +
    #     base.group_user rw access for the new model.
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
    'depends': ['base_setup', 'mrp', 'mrp_plm', 'mrp_workorder', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_material_request_m_studio_ported.xml',
        'views/mrp_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}