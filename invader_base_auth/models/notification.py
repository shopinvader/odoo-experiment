# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models
from odoo.tools.translate import _


class ShopinvaderNotification(models.Model):
    _inherit = "shopinvader.notification"

    def _get_all_notification(self):
        res = super(ShopinvaderNotification, self)._get_all_notification()
        res.update(
            {
                "request_reset_password": {
                    "name": _("Request password reset"),
                    "model": "res.partner",
                },
            }
        )
        return res
