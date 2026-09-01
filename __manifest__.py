# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : MRP',
    'version': '17.0.0.0.22',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.22: view 2324 mrp.workcenter form (6986b) - inserts full nested
    # form for equipment_ids O2M, adds "Actual Costing" group + "Users" tab.
    # See views/mrp_studio_ported_v4.xml.
    #   * ZERO field ports needed. All 17 nested-form fields exist on
    #     maintenance.equipment (relation of equipment_ids), pinned to
    #     maintenance/hr_maintenance/mrp_maintenance/BugFix-Maintenance.
    #     Modifier refs "department"/"employee" are Selection VALUES for
    #     equipment_assign_to, not field names -> no sentinels.
    #   * 1 numeric button ref converted: 667 ->
    #     %(maintenance.hr_equipment_request_action_from_equipment)d.
    # New deps: maintenance, hr_maintenance, mrp_maintenance,
    # BugFix-Maintenance. BugFix-Maintenance depends only on
    # [base_setup, maintenance] -- adding this edge stays acyclic.
    # v0.0.21: view 4830 mrp.eco form (1634b) + 2 field ports on mrp.eco.
    # See views/mrp_studio_ported_v3.xml.
    #   * models/mrp_eco.py: x_studio_error (Char) + x_studio_tag_description
    #     (Char) added alongside v0.0.18's x_studio_item_approved boolean.
    #   * 4830 form: byte-verbatim Studio arch. 8 xpath positions
    #     (approve/action_apply approval-gating, product_tmpl_id, bom_id x2,
    #     effectivity, tag_ids x2). 2 sentinels injected for state + type.
    #   * studio_approval attribute on 2 buttons preserved -- Studio-specific
    #     approval-gating behaviour. Fallback plan: strip those xpaths if
    #     Odoo rejects the attribute (Odoo validation is permissive so
    #     expected OK).
    # v0.0.20: hardcoded-ref button-views on mrp.bom + mrp.production +
    # restored 3953. See views/mrp_studio_ported_v2.xml.
    #   * 4 code-state server actions ported to data/server_actions.xml:
    #     - 1057 Update Costs in BOM (on mrp.bom)
    #     - 1147 Mass Produce Serial Numbers (on mrp.production)
    #     - 2534 Finished Products Location Updated (on mrp.production)
    #     - 3202 Mass Produce Serial Numbers - Cancel Serial No (on mrp.production)
    #     All 4 reference custom models (x_mrp_bom_material_cos, x_mass_produce_serial,
    #     etc.) via lazy env['x_...'] lookups; safe at install, runtime button
    #     clicks may fail until those models are ported.
    #   * 3945 mrp.bom form: "Update Cost" button in header (references 1057).
    #   * 3946 mrp.production form: 3 buttons + 6 button-attribute overrides
    #     (Mass Produce/Update/Cancel Serial). References 1147, 2534, 3202.
    #     7 sentinel <field invisible="1"/> injected for x_studio_* fields
    #     referenced in modifier expressions.
    #   * 3953 mrp.workorder tablet form: RESTORED from v0.0.18 rollback.
    #     Enabled by new BugFix-Stock dep -- stock.lot.x_studio_production_id
    #     now resolves at BugFix-MRP install time.
    # New deps: BugFix-Stock (for 3953 domain field), mrp_workorder
    # (for 3953 inherit target). BugFix-Stock has no dep on any BugFix-*
    # repo -- adding this edge stays acyclic (verified against manifest).
    # v0.0.19: v0.0.18 minus view 3953 (mrp.workorder tablet form).
    # 3953's domain references stock.lot.x_studio_production_id which
    # is pinned to BugFix-Stock. Not in our depends chain -> field not
    # yet in registry at BugFix-MRP install time -> "Unknown field in
    # domain" ParseError. Rolled back cleanly. mrp_workorder dep also
    # dropped -- was only added for 3953. Decision needed on 3953:
    # add BugFix-Stock cross-repo dep, or defer permanently.
    # v0.0.18: bulk of small Studio inherits on standard mrp.* models
    # (SEE ROLLBACK ABOVE). Ported 4 clean views + 1 that failed.
    #   * 2390 mrp.production.tree                 (486b)  OK
    #   * 5503 mrp.workcenter.productivity.tree    (277b)  OK
    #   * 3151 mrp.workcenter.tree                 (620b)  OK
    #   * 5062 mrp.eco.view.tree                   (278b)  OK
    #   * 3953 mrp.workorder.view.form (tablet)    (642b)  FAILED
    # New model file mrp_eco.py declares x_studio_item_approved (boolean).
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
    'depends': ['base_setup', 'mrp', 'mrp_plm', 'mrp_workorder', 'maintenance', 'hr_maintenance', 'mrp_maintenance', 'BugFix-Stock', 'BugFix-Maintenance', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_material_request_m_studio_ported.xml',
        'views/mrp_studio_ported.xml',
        'views/mrp_studio_ported_v2.xml',
        'views/mrp_studio_ported_v3.xml',
        'views/mrp_studio_ported_v4.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}