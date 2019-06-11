# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Benoît GUILLOT <benoit.guillot@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo.addons.shopinvader.tests.common import ProductCommonCase


class ProductCase(ProductCommonCase):
    def test_create_binding_with_attribute(self):
        self.white_color = self.env.ref("product.product_attribute_value_3")
        product = (
            self.env["shopinvader.product"]
            .with_context(map_children=True)
            .create(
                {
                    "lang_id": self.backend.lang_ids[0].id,
                    "bakend_id": self.backend.id,
                    "display_value_ids": [(6, 0, [self.white_color.id])],
                    "record_id": self.template.id,
                }
            )
        )
        variants = product.shopinvader_variant_ids
        self.assertEqual(product.url_key, "ipad-retina-display-white")
        self.assertEqual(len(variants), 2)
        self.assertEqual(variants[0].main, True)
        self.assertEqual(variants[1].main, False)

    def test_model_id(self):
        self.assertEqual(self.shopinvader_variant.model_id, self.template.id)
