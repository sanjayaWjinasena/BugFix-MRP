# BugFix-MRP — views to hand-port

22 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 8747 | calendar | `x_material_request_m` | Default calendar view for x_material_request_m | — |
| 2 | 8745 | form | `x_material_request_m` | Default form view for x_material_request_m | — |
| 3 | 8748 | gantt | `x_material_request_m` | Default gantt view for x_material_request_m | — |
| 4 | 8752 | graph | `x_material_request_m` | Default graph view for x_material_request_m | — |
| 5 | 8749 | kanban | `x_material_request_m` | Default kanban view for x_material_request_m | — |
| 6 | 8744 | tree | `x_material_request_m` | Default list view for x_material_request_m | — |
| 7 | 8750 | map | `x_material_request_m` | Default map view for x_material_request_m | — |
| 8 | 8751 | pivot | `x_material_request_m` | Default pivot view for x_material_request_m | — |
| 9 | 8746 | search | `x_material_request_m` | Default search view for x_material_request_m | — |
| 10 | 2574 | form | `mrp.bom` | Odoo Studio: mrp.bom.form customization | mrp.bom.form |
| 11 | 3945 | form | `mrp.bom` | Odoo Studio: mrp.bom.form customization-button | mrp.bom.form |
| 12 | 5461 | tree | `mrp.bom` | Odoo Studio: mrp.bom.tree customization | mrp.bom.tree |
| 13 | 4830 | form | `mrp.eco` | Odoo Studio: mrp.eco.view.form customization | mrp.eco.view.form |
| 14 | 5062 | tree | `mrp.eco` | Odoo Studio: mrp.eco.view.tree customization | mrp.eco.view.tree |
| 15 | 2325 | form | `mrp.production` | Odoo Studio: mrp.production.form customization | mrp.production.form |
| 16 | 3946 | form | `mrp.production` | Odoo Studio: mrp.production.form-button | mrp.production.form |
| 17 | 2390 | tree | `mrp.production` | Odoo Studio: mrp.production.tree customization | mrp.production.tree |
| 18 | 2324 | form | `mrp.workcenter` | Odoo Studio: mrp.workcenter.form customization | mrp.workcenter.form |
| 19 | 5503 | tree | `mrp.workcenter.productivity` | Odoo Studio: mrp.workcenter.productivity.tree customization | mrp.workcenter.productivity.tree |
| 20 | 3151 | tree | `mrp.workcenter` | Odoo Studio: mrp.workcenter.tree customization | mrp.workcenter.tree |
| 21 | 5063 | form | `mrp.eco` | mrp.eco.view.form_button | mrp.eco.view.form |
| 22 | 3953 | form | `mrp.workorder` | mrp.workorder.view.form.inherit.quality.tablet.new-button | mrp.workorder.view.form.inherit.quality.tablet.new |
