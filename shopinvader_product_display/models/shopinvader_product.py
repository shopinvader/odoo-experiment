# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class ShopinvaderProduct(models.Model):
    _inherit = "shopinvader.product"

    display_value_ids = fields.Many2many(
        comodel_name="product.attribute.value", string="Attribute"
    )
    available_attribute_value_ids = fields.Many2many(
        "product.attribute.value",
        string="Attributes",
        compute="_compute_available_attribute",
    )
    attribute_identifier = fields.Char(
        compute="_compute_attribute_indentifier"
    )
    model_id = fields.Integer(
        compute="_compute_model_id", store=True, index=True
    )

    @api.depends("record_id")
    def _compute_model_id(self):
        for record in self:
            record.model_id = record.record_id.id

    def _get_url_keywords(self):
        keyword = super(ShopinvaderProduct, self)._get_url_keywords()
        for attribute in self.display_value_ids:
            keyword.insert(1, attribute.name)
        return keyword

    # backend_id is only here to trigger the onchange when creating a new
    # binding
    @api.depends("backend_id", "record_id.attribute_line_ids.value_ids")
    def _compute_available_attribute(self):
        for rec in self:
            rec.available_attribute_value_ids = rec.record_id.mapped(
                "attribute_line_ids.value_ids"
            )

    def _compute_attribute_identifier(self):
        for record in self:
            ids = record.display_value_ids.ids
            ids.sort()
            record.attribute_identifier = ",".join(ids)

    def _get_variants(self):
        variants = super(ShopinvaderProduct, self)._get_variants()
        if self.display_value_ids:
            filtered_variants = self.env["product.product"].browse()
            for variant in super(ShopinvaderProduct, self)._get_variants():
                if self.display_value_ids < variant.attribute_value_ids:
                    filtered_variants |= variant
            return filtered_variants
        else:
            return variants

    _sql_constraints = [
        (
            "record_uniq",
            "unique(backend_id, record_id, lang_id, attribute_identifier)",
            "A product can only have one binding by backend "
            "and lang and attribute.",
        )
    ]
