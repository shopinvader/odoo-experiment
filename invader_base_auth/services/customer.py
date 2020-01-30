# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import uuid
import datetime

from odoo.addons.component.core import Component
from odoo import fields
from odoo.osv import expression
from odoo.exceptions import UserError
from odoo.tools.translate import _


TOKEN_VALIDITY_INTERVAL = datetime.timedelta(hours=48)


class InvaderCustomerService(Component):
    _inherit = "shopinvader.customer.service"

    def sign_in(self, **params):
        res = super(InvaderCustomerService, self).sign_in(**params)
        return res

    def reset_password(self, **params):
        raise NotImplementedError

    def request_reset_password(self, **params):
        domain = self._get_base_search_domain()
        domain = expression.AND([domain, [("email", "=", params["email"])]])
        customer = self.env["shopinvader.partner"].search(domain)
        if len(customer) != 1:
            # Do not reveal if there is an account for this e-mail address
            return {}
        customer.write(
            {
                "password_reset_token": uuid.uuid4(),
                "password_reset_token_date": datetime.datetime.now(),
            }
        )
        self.shopinvader_backend._send_notification(
            "request_reset_password", customer
        )
        return {}

    def reset_password(self, **params):
        """
        The password is not altered in this function.
        It needs to be inhereted in order to actually do it
        """
        domain = self._get_base_search_domain()
        domain = expression.AND(
            [
                domain,
                [
                    ("password_reset_token", "=", params["token"]),
                    (
                        "password_reset_token_date",
                        ">=",
                        fields.Datetime.to_string(
                            datetime.datetime.now() - TOKEN_VALIDITY_INTERVAL
                        ),
                    ),
                ],
            ]
        )
        customer = self.env["shopinvader.partner"].search(domain)
        if len(customer) != 1:
            raise UserError(
                _(
                    u"The link you are trying to use is expired."
                    " Please request a new one."
                )
            )
        customer.write(
            {"password_reset_token": None, "password_reset_token_date": None,}
        )
        self.work.partner = customer.record_id
        return self._assign_cart_and_get_store_cache()

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

    def _validator_request_reset_password(self):
        return {
            "email": {"type": "string", "required": True},
        }

    def _validator_reset_password(self):
        return {
            "token": {"type": "string", "required": True},
            "password": {"type": "string", "required": True},
        }

    def _validator_sign_out(self):
        return {}
