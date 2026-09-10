from . import mrp_bom
from . import mrp_eco
from . import mrp_production
from . import mrp_workcenter
from . import mrp_workcenter_productivity
from . import mrp_workorder
from . import x_material_request_m
from . import x_material_request_m_line_af405
from . import x_material_request_m_stage
from . import x_material_request_m_tag
from . import x_mass_produce_serial
from . import x_mass_produce_serial_line
from . import x_mrp_bom_general_cost
from . import x_mrp_bom_labour_cost
from . import x_mrp_bom_material_cos
from . import x_mrp_bom_overhead_cos
# x_sales_report_type sentinel removed: Jinasena_Masterdata_Reporting
# now owns the model. Many2one ref on mrp.production resolves at
# load time via the new dep.

from . import mrp_eco_gap
from . import x_mass_produce_serial_gap
from . import x_mass_produce_serial__gap
from . import x_material_request_m_gap
from . import x_material_request_m_line_af405_gap
from . import x_material_request_m_stage_gap
from . import x_material_request_m_tag_gap
from . import x_mrp_bom_general_cost_gap
from . import x_mrp_bom_labour_cost_gap
from . import x_mrp_bom_material_cos_gap
from . import x_mrp_bom_overhead_cos_gap
