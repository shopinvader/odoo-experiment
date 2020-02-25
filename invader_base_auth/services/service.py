# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.component.core import AbstractComponent

class BaseShopinvaderService(AbstractComponent):
    _inherit = "base.shopinvader.service"

    def dispatch(self, method_name, _id=None, params=None):
        if self.partner == False:
            service = self.work.component(usage="customer")
            return service.sign_out()
        return super(BaseShopinvaderService, self).dispatch(method_name, _id=_id, params=params)
