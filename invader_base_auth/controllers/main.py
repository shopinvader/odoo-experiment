# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.shopinvader.controllers import main
from odoo.exceptions import MissingError

class InvaderController(main.InvaderController):

    @classmethod
    def _get_partner_from_headers(cls, headers):
        try:
            res = super(InvaderController, cls)._get_partner_from_headers(headers)
        except MissingError:
            # Continue if there is an error to allow signing out if the
            # partner is unknown
            return False
