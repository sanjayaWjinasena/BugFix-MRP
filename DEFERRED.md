# BugFix-MRP — Deferred Items

Items intentionally not ported yet. Each entry documents WHY the deferral,
what would need to happen to un-defer, and any current-state observations
so a future session can pick up without re-triaging.

---

## View 2325 — mrp.production form (27336b) — Studio inherit

**Studio xmlid:** studio_customization (default_form_view_mrp_production_UUID)
**Model:** mrp.production
**Inherit target:** mrp.mrp_production_form_view

**Why deferred (2026-09-01):**
This is a 27KB form-inherit that inserts fields into deeply nested xpath
contexts (targeting into workorder_ids tree, move_raw_ids form,
quality_check tree, etc.). Cannot be ported in one batch because it
depends on multiple custom sub-models that don't exist on-disk yet.

**Scout scoreboard (from v0.0.23 investigation):**
- 29 x_studio_ fields already ported to models/mrp_production.py.
- 10 studio_approval attributes (like v0.0.21's 4830 pattern — expected OK).
- 1 hardcoded ref: `617` (Block Workcenter — mrp.act_mrp_block_workcenter_wo,
  exists on repair-test-101). Easy interpolation.
- External pins encountered in field refs: `mrp`, `mrp_workorder`, `quality`,
  `quality_mrp`, `quality_mrp_workorder`, `stock`. Need to add
  `quality_mrp` + `quality_mrp_workorder` deps if any field refs land in
  those contexts.

**Custom sub-models referenced (need porting before 2325 can land):**
Roughly:
- `x_mrp_bom_material_cos` (already referenced by server action 1057 in v0.0.20)
- `x_mrp_bom_labour_cost`
- `x_mrp_bom_overhead_cos`
- `x_mrp_bom_general_cost`
- `x_mrp_prod_bom_material_cos`
- `x_mrp_prod_bom_labour_cost`
- `x_mrp_prod_bom_overhead_cos`
- `x_mrp_prod_bom_general_cost`
- `x_mass_produce_serial` (already referenced by server action 1147 in v0.0.20)
- Possibly others (need RPC dump of Clear-DB `x_mrp_*` models to enumerate)

**Un-defer prerequisite chain (proposed):**
1. Enumerate all custom `x_mrp_*` models on Clear-DB via
   `env['ir.model'].search([('model', 'like', 'x_mrp_%')])`.
2. Port each as a dedicated Python class + O2M inverse fields on
   mrp.production / mrp.bom.
3. Once sub-models exist, RE-SCOUT 2325 to see the residual field-port
   need on mrp.production itself (should shrink significantly).
4. Port remaining mrp.production fields.
5. Ship 2325 with proper `%(...)d` interpolation for ref 617 and any
   sentinels required by strict-modifier validation.

**Sizing:** Likely 3-5 versions of work total. Blocks 2574 mrp.bom
(6140b) also since they share the same cost sub-models.

**Cost of premature attempt (ping-pong debug):**
See feedback-clear-db-verbatim + feedback-cross-repo-field-ref memories.
The Clear-DB rule "never assume Clear-DB is permissive" applies — Odoo 17
strict validation will produce iteration cycles measured in install
attempts, not minutes.

---

## View 2574 — mrp.bom form (6140b) — Studio inherit

**Studio xmlid:** studio_customization (default_form_view_mrp_bom_UUID)
**Model:** mrp.bom
**Inherit target:** mrp.mrp_bom_form_view

**Why deferred (2026-09-01):**
Similar to 2325 — arch references multiple custom cost sub-models
(`x_mrp_bom_material_cos`, `x_mrp_bom_labour_cost`, `x_mrp_bom_overhead_cos`,
`x_mrp_bom_general_cost`) that need to be ported before the view can
compose. 17 fields flagged missing on mrp.bom in initial scout, but real
count is smaller once nested-form fields are excluded (my scout was too
naive — same class of false positives as 2325).

**Hardcoded ref:** 1057 (Update Costs in BOM — already ported in v0.0.20
as `%(BugFix-MRP.server_action_1057_update_costs_in_bom)d`).

**Un-defer prerequisite chain (proposed):**
1. Port the 4 `x_mrp_bom_*_cost` custom models (shared with 2325
   prerequisite chain).
2. Re-scout 2574 to see residual field-port need on mrp.bom.
3. Ship.

**Sizing:** 1-2 versions after custom models land.

---

## Cross-repo runtime deferrals (from v0.0.20)

**Server action 1057 (Update Costs in BOM)** references custom models
`x_mrp_bom_material_cos`, `x_mrp_bom_labour_cost`, `x_mrp_bom_overhead_cos`,
`x_mrp_bom_general_cost`. Install succeeds (lazy `env['x_...']` eval),
runtime button click fails until models are ported.

**Server action 1147 (Mass Produce Serial Numbers)** references
`x_mass_produce_serial` wizard model. Install succeeds, runtime fails
until model ported.

**Server action 3202 (Cancel Serial No)** references
`stock.lot.x_studio_production_id` — already resolved via BugFix-Stock
dep (v0.0.20). Runtime should work as long as stock.lot pin holds.

---

## History of resolved deferrals (kept for continuity)

- **View 3953 mrp.workorder tablet form** — deferred v0.0.18-v0.0.19 due
  to cross-repo field ref on `stock.lot.x_studio_production_id`.
  Resolved v0.0.20 by adding `BugFix-Stock` dep to manifest.
- **View 4830 mrp.eco form** — deferred through v0.0.19-v0.0.20 pending
  small field-port work. Landed v0.0.21 (2 Char field ports).
- **View 2324 mrp.workcenter form** — flagged as "needs re-scout" in
  v0.0.20 triage; scoped and shipped v0.0.22 (zero field ports, all
  fields lived on maintenance.equipment).
