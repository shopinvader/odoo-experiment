# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ShopinvaderPartner(models.Model):
    _inherit = "shopinvader.partner"

    password_reset_token = fields.Char()
    password_reset_token_date = fields.Datetime()
