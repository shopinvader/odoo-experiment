# -*- coding: utf-8 -*-
# Copyright 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader Product Display",
    "version": "10.0.0.0.0",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["shopinvader"],
    "data": [
        "views/shopinvader_product_views.xml",
        "views/product_attribute_views.xml",
        "data/ir_export_product.xml",
    ],
    "demo": [],
    "qweb": [],
}
