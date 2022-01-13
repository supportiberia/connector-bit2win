# -*- coding: utf-8 -*-
# Part of Rapsodoo Iberia.

from odoo import models, fields, _
import base64


class Sale(models.Model):
    _inherit = 'sale.order'

