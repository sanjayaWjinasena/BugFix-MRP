# BugFix-MRP — Deferred Items

**Status: EMPTY.** All previously-deferred items shipped across v0.0.23–v0.0.27.

This file remains as documentation of the arc — see "History of resolved
deferrals" below for the sequence.

---

## Current backlog

None. If a new deferral surfaces during future work, document it above this
line with the pattern used in the resolved section below (Why deferred +
prerequisite chain + sizing).

---

## History of resolved deferrals

- **View 3953 mrp.workorder tablet form** — deferred v0.0.18–v0.0.19 due
  to cross-repo field ref on `stock.lot.x_studio_production_id`.
  Resolved v0.0.20 by adding `BugFix-Stock` dep to manifest.
- **View 4830 mrp.eco form** — deferred through v0.0.19–v0.0.20 pending
  small field-port work. Landed v0.0.21 (2 Char field ports).
- **View 2324 mrp.workcenter form** — flagged as "needs re-scout" in
  v0.0.20 triage; scoped and shipped v0.0.22 (zero field ports, all
  fields lived on maintenance.equipment).
- **View 2574 mrp.bom form (6140b)** — deferred pending 4 custom cost
  sub-models (x_mrp_bom_*_cost). Resolved v0.0.24 after v0.0.23 shipped
  the foundation.
- **View 2325 mrp.production form (27336b)** — THE big one. Deferred
  pending same 4 cost sub-models + O2M inverses on mrp.production.
  Resolved v0.0.25 after v0.0.23 shipped foundation. Added 5 new deps
  (quality/quality_mrp/quality_mrp_workorder/purchase_stock/stock_delivery).
- **Server action 1147 (Mass Produce Serial Nos) runtime deferral** —
  referenced `x_mass_produce_serial` wizard model that wasn't ported at
  ship time. Resolved v0.0.26 (2 wizard models + 3 backing server
  actions 1149/1150/1151 + primary form view 2600 + Studio inherit 5898).
- **v0.0.26 install failure (KeyError on inverse_name)** — parent O2M
  targeted wrong comodel string (`x_mass_produce_serial_line` file name
  vs `_` trailing-underscore _name). Hotfixed v0.0.27. Saved memory
  feedback-studio-truncated-model-names.
- **Server actions 1057 (Update Costs in BOM) runtime deferral** —
  referenced 4 x_mrp_bom_*_cost custom models. Resolved v0.0.23 by
  porting those models. No code change to 1057 needed (it lazy-evals
  env['x_...']).

## Related memories

- [[feedback-cross-repo-field-ref]] — the 3953 dep-chain lesson
- [[feedback-hardcoded-action-ids]] — the button-name interpolation
  pattern used throughout
- [[feedback-strict-modifier-sentinels]] — sentinel injection pattern
- [[feedback-studio-truncated-model-names]] — the v0.0.26 comodel-name
  lesson
- [[feedback-clear-db-verbatim]] — the "always verify pin source" rule
