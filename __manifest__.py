# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : MRP',
    'version': '17.0.0.0.26',
    'summary': 'Studio-to-Python port for BugFix-MRP',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Manufacturing',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.26: x_mass_produce_serial wizard - un-defers server action 1147
    # (Mass Produce Serial Nos button on 3946 mrp.production form) end-to-end.
    # Completes the runtime deferrals list from DEFERRED.md.
    #   * models/x_mass_produce_serial.py (14 fields, parent wizard)
    #   * models/x_mass_produce_serial_line.py (16 fields, line records.
    #     Model _name = 'x_mass_produce_serial_' with trailing underscore
    #     -- Studio truncated at 24-char model-name limit).
    #   * 3 new server actions in data/server_actions.xml:
    #     1149 Generate  - creates line records for the requested serial range
    #     1150 Clear     - deletes lines and resets prefix/sequence fields
    #     1151 Create Original Serial No - creates stock.lot records from lines
    #                                       + marks mrp.production as mass_produced
    #   * views/x_mass_produce_serial_studio_ported.xml: primary form
    #     (view 2600) + Studio inherit (view 5898). Byte-verbatim except 3
    #     hardcoded numeric refs (1149/1150/1151) interpolated to xmlids.
    #   * security/ir_model_pins.xml + ir.model.access.csv: 2 model pin
    #     records + 2 base.group_user ACL rows.
    # No new deps required. All external refs (stock.lot, res.company,
    # product.product, uom.uom, mrp.production) already covered by
    # existing dep chain.
    # v0.0.25: view 2325 mrp.production form (27336b) - THE big DEFERRED.md
    # item. Un-defers cleanly now that v0.0.23 shipped cost sub-models +
    # O2M inverses. See views/mrp_studio_ported_v6.xml.
    #   * 1 hardcoded ref converted: 617 -> %(mrp.act_mrp_block_workcenter_wo)d.
    #   * 0 field ports needed (all refs resolve post-v0.0.23; 145 unique
    #     refs across 7 models -- re-scout confirmed zero real missing).
    #   * 0 sentinels needed.
    #   * 10 studio_approval attributes preserved (tolerated).
    # View adds: full nested form+tree for workorder_ids (tablet-mode
    # workorder UI with time_ids/check_ids/finished_lot sub-elements),
    # nested form for move_raw_ids (Stock Moves detail view), and 5
    # notebook tabs (Direct Material/Labour/Overhead/General Cost + Costing
    # summary) matching the mrp.bom form tabs pattern.
    # New deps: purchase_stock, quality, quality_mrp, quality_mrp_workorder,
    # stock_delivery. All 5 confirmed installed on repair-test-101.
    # None have BugFix-* deps, so all edges stay acyclic.
    # v0.0.24: view 2574 mrp.bom form (6140b) - un-defers the DEFERRED.md
    # item now that v0.0.23 shipped the cost sub-model foundation.
    # See views/mrp_studio_ported_v5.xml.
    #   * 1 hardcoded ref converted: 1057 ->
    #     %(BugFix-MRP.server_action_1057_update_costs_in_bom)d.
    #   * 0 field ports (all refs resolve post-v0.0.23).
    #   * 0 sentinels needed. 0 studio_approval attributes.
    #   * View adds 5 notebook tabs to mrp.bom form: Direct Material Cost,
    #     Direct Labour Cost, Direct Overhead Cost, Direct General Cost, Costing.
    #     Also inserts a routing-workcenter tree into //field[@name='operation_ids']
    #     with 5 fields on mrp.routing.workcenter (all state=base).
    # v0.0.23: 4 custom cost sub-models + 8 parent O2M inverses.
    # Foundation ships; views 2325 + 2574 land in later versions.
    #   * models/x_mrp_bom_material_cos.py  (17 fields, 1805 Clear-DB rows)
    #   * models/x_mrp_bom_labour_cost.py   (17 fields, 1605 rows)
    #   * models/x_mrp_bom_overhead_cos.py  (13 fields, 1605 rows)
    #   * models/x_mrp_bom_general_cost.py  (13 fields, 1605 rows)
    # Model names truncated to 24 chars per Studio quirk (_cos not _cost
    # for material + overhead). Each child has 2 parent M2Os:
    # x_studio_bom_*_cost_ids (-> mrp.bom, cascade) and
    # x_studio_prod_bom_*_cost_ids (-> mrp.production, cascade), plus
    # operation_id, prod_bom_line_id refs.
    #   * models/mrp_bom.py: 4 TODO O2Ms un-TODO'd with proper inverse
    #     names (x_studio_direct_general_cost, x_studio_one2many_field_
    #     4rhw9/bOopH/jPlQP -- names verbatim from Studio).
    #   * models/mrp_production.py: 4 TODO O2Ms un-TODO'd similarly
    #     (x_studio_direct_general_cost, x_studio_direct_material_cost,
    #     x_studio_one2many_field_Fzcvl/vg1OS).
    #   * security/ir_model_pins.xml + ir.model.access.csv: 4 model pin
    #     records + 4 base.group_user ACL rows.
    # Unblocks: server action 1057 runtime (Update Costs in BOM),
    # server action 1057's env['x_mrp_bom_*_cost'] lookups now resolve.
    # Doesn't ship views yet -- 2325 and 2574 need further re-scout to
    # confirm all fields resolve now that parent O2Ms exist.
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
    'depends': ['base_setup', 'mrp', 'mrp_plm', 'mrp_workorder', 'maintenance', 'hr_maintenance', 'mrp_maintenance', 'purchase_stock', 'quality', 'quality_mrp', 'quality_mrp_workorder', 'stock_delivery', 'BugFix-Stock', 'BugFix-Maintenance', 'Jinasena_Masterdata_Reporting'],
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
        'views/mrp_studio_ported_v5.xml',
        'views/mrp_studio_ported_v6.xml',
        'views/x_mass_produce_serial_studio_ported.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}