# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component


class InvaderCustomerService(Component):
    _inherit = "shopinvader.customer.service"

    def sign_in(self, **params):
        res = super(InvaderCustomerService, self).sign_in(**params)
        return res

    def reset_password(self, **params):
        raise NotImplementedError

    def sign_out(self, **params):
        self.shopinvader_response.reset()
        res = {}
        res["store_cache"] = {"customer": {}}
        res["set_session"] = {"cart_id": 0}
        return res

    def _validator_sign_in(self):
        return {
            "login": {"type": "string", "required": True},
            "password": {"type": "string", "required": True},
        }

    def _validator_reset_password(self):
        return {
            "login": {"type": "string", "required": True},
            "password": {"type": "string", "required": True},
            "new_password": {"type": "string", "required": True},
        }

    def _validator_sign_out(self):
        return {}
