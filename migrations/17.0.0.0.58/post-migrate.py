# -*- coding: utf-8 -*-
"""BugFix-MRP v17.0.0.0.58: seed ir.model.fields.selection rows via ORM.

Same content as post_init_hook in ../hooks.py; this covers the version-upgrade
path (post-migrate runs on upgrade; hooks.py runs on fresh install). Uses the
ORM (no direct SQL) per the project's no-direct-SQL rule.

Idempotent: skips rows whose (field_id, value) already exists.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

_FIELD_SELECTIONS = [
    ('x_material_request_m', 'x_studio_kanban_state', 'normal', 'In Progress', 10),
    ('x_material_request_m', 'x_studio_kanban_state', 'done', 'Ready', 1),
    ('x_material_request_m', 'x_studio_kanban_state', 'blocked', 'Blocked', 2),
]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Fld = env['ir.model.fields']
    Sel = env['ir.model.fields.selection']
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-MRP v17.0.0.0.58: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )
