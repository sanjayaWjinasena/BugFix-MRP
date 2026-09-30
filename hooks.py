# -*- coding: utf-8 -*-
"""BugFix-MRP: post-install hooks.

Seeds ir.model.fields.selection rows that Studio populated in CDB but
Odoo 17 doesn't recreate on install. Uses the ORM (no direct SQL) per the
project's no-direct-SQL rule; the sibling migrations/<v>/post-migrate.py
runs the same seeding on version upgrades.
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seed data (ORM-only, no direct SQL) ---
# All rows Studio populated in CDB but Odoo 17 doesn't recreate on install.
# `state='base'` rows: options for Python-declared Selection fields that
# Odoo would normally set at install but Studio-side sequence differs.
# `related=` rows: audit-parity stubs — Odoo resolves at runtime from the
# source field, so shipping these creates DB rows for audit match with zero
# functional effect. (See feedback-python-only-fixes: prefer ORM over SQL.)
# (model, field_name, value, display_name, sequence)
_FIELD_SELECTIONS = [
    ('x_material_request_m', 'x_studio_kanban_state', 'normal', 'In Progress', 10),
    ('x_material_request_m', 'x_studio_kanban_state', 'done', 'Ready', 1),
    ('x_material_request_m', 'x_studio_kanban_state', 'blocked', 'Blocked', 2),
]


def _seed_field_selections(env, entries):
    """Idempotent ORM create of ir.model.fields.selection rows.
    Skip if the field is absent or the (field, value) row already exists.
    Per-row savepoint so a single failure doesn't abort the batch."""
    Fld = env['ir.model.fields'].sudo()
    Sel = env['ir.model.fields.selection'].sudo()
    for model, fname, value, label, seq in entries:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-MRP: seed skip %s.%s (field absent).", model, fname,
            )
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with env.cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-MRP: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
