# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import Component
from odoo.exceptions import UserError
from odoo.tools.translate import _


class InvaderCustomerService(Component):
    _inherit = "shopinvader.customer.service"

    def sign_in(self, **params):
        Ldap = self.env["res.company.ldap"]
        self.work.partner = self.env["shopinvader.partner"].search(
            [("email", "=", params["login"])]
        )
        if len(self.partner) != 1:
            raise UserError(
                _(
                    "Impossible to log in. Either your password is wrong "
                    "or your account does not exist."
                )
            )
        for conf in Ldap.get_ldap_dicts():
            if Ldap.authenticate(conf, params["login"], params["password"]):
                return super(InvaderCustomerService, self).sign_in(
                    **params
                )
        raise UserError(
            _(
                "Impossible to log in. Either your password is wrong "
                "or your account does not exist."
            )
        )
