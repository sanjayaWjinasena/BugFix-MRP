from odoo import api, fields, models

# MO header buttons hidden for now (bug sheet, Manufacturing row 7,
# 20/Oct: "Temporarily remove these buttons"). Matched by button name
# first and by label as a fallback, so a renamed core method still hides.
_HIDDEN_MO_BUTTON_NAMES = (
    "button_maintenance_req",  # Maintenance Request (mrp_maintenance)
    "action_open_label_type",  # Print Labels
    "action_open_label_layout",  # Print Labels (older name)
)
# 'Unlock' is matched by label only: the Lock button shares its method.
_HIDDEN_MO_BUTTON_LABELS = ("Maintenance Request", "Print Labels", "Unlock")


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    mrp_current_user = fields.Many2one(
        "res.users", string="Current User", readonly=True
    )
    direct_general_cost = fields.One2many(
        "mrp_bom_general_cost",
        "prod_bom_general_cost_ids",
        string="Direct General Cost",
    )
    direct_material_cost = fields.One2many(
        "mrp_bom_material_cos",
        "prod_bom_material_cost_ids",
        string="Direct Material Cost",
    )
    finished_product_location = fields.Many2one(
        "stock.location", string="Finished Product Location"
    )
    finished_products_location_updated = fields.Boolean(
        string="Finished Products Location Updated"
    )
    grand_total_actual_cost_1 = fields.Float(
        string="Grand Total (Actual Cost)", readonly=True
    )
    grand_total_planned_cost = fields.Float(
        string="Grand Total (Planned Cost)", readonly=True
    )
    mark_as_done_validation = fields.Text(string="Mark as Done Validation")
    mass_produced = fields.Boolean(string="Mass Produced")
    melt_item = fields.Boolean(string="Melt Item", readonly=True)
    one2many_field_Fzcvl = fields.One2many(
        "mrp_bom_labour_cost",
        "prod_bom_labour_cost_ids",
        string="Direct Labour Cost",
    )
    one2many_field_vg1OS = fields.One2many(
        "mrp_bom_overhead_cos",
        "prod_bom_overhead_cost_ids",
        string="Direct Overhead Cost",
    )
    original_mo = fields.Char(string="Original MO")
    ot_applicable = fields.Boolean(
        string="OT  Applicable", readonly=True, store=False
    )
    pro_bom_total_general_cost = fields.Float(
        string="Total General Cost", readonly=True
    )
    process_error = fields.Text(string="Process Error")
    prod_bom_total_actual_labour_cost = fields.Float(
        string="Total Actual Labour Cost", readonly=True
    )
    prod_bom_total_actual_labour_cost_ot = fields.Float(
        string="Total Actual Labour Cost (OT)", readonly=True
    )
    prod_bom_total_actual_labour_cost_without_ot = fields.Float(
        string="Total Actual Labour Cost (Without OT)", readonly=True
    )
    prod_bom_total_actual_material_cost = fields.Float(
        string="Total  Actual Material Cost", readonly=True
    )
    prod_bom_total_actual_overhead_cost = fields.Float(
        string="Total Actual Overhead Cost", readonly=True
    )
    prod_bom_total_labour_cost = fields.Float(
        string="Total Labour Cost", readonly=True
    )
    prod_bom_total_material_cost = fields.Float(
        string="Total Material Cost", readonly=True
    )
    prod_bom_total_overhead_cost = fields.Float(
        string="Total Overhead Cost", readonly=True
    )
    quantity_validation = fields.Boolean(
        string="Quantity Validation", readonly=True, store=False
    )
    report_type_m_wip = fields.Many2one(
        "sales_report_type", string="Report Type (M-WIP)"
    )
    serial_cancelled = fields.Boolean(string="Serial Cancelled")
    source_validate = fields.Boolean(
        string="Source Validate",
        readonly=True,
        store=False,
        compute="_compute_source_validate",
    )
    super_user = fields.Boolean(
        string="Super User", readonly=True, store=False
    )
    super_user_melt_items = fields.Boolean(
        string="Super User (Melt Items)", readonly=True
    )
    temp_location = fields.Boolean(string="Temp Location", readonly=True)
    total_actual_general_cost = fields.Float(
        string="Total Actual General Cost", readonly=True
    )
    tracked_item = fields.Boolean(
        string="Tracked Item",
        readonly=True,
        store=False,
        compute="_compute_tracked_item",
    )

    # Ported verbatim from the Clear-DB Studio computes (same depends). Without them both flags
    # stayed False, so the "Mass Produce Serial Nos" button never showed for serial-tracked products.
    @api.depends("product_id")
    def _compute_tracked_item(self):
        for rec in self:
            rec.tracked_item = rec.product_id.tracking == "serial"

    @api.depends("origin")
    def _compute_source_validate(self):
        for rec in self:
            val = False
            if rec.origin:
                if rec.origin == "MPS" or rec.origin.startswith("OP"):
                    val = True
            if rec.location_src_id.id != rec.location_dest_id.id:
                val = True
            rec.source_validate = val

    @api.model
    def _get_view(self, view_id=None, view_type="form", **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type == "form":
            for btn in arch.xpath("//header//button"):
                if (
                    btn.get("name") in _HIDDEN_MO_BUTTON_NAMES
                    or btn.get("string") in _HIDDEN_MO_BUTTON_LABELS
                ):
                    btn.set("invisible", "1")
        return arch, view
