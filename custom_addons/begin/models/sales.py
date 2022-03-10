# -*- coding: utf-8 -*-


from odoo import models, fields, api



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # _description = 'pranali_work.pranali_work'

    customer_id = fields.Char(string="customer Id")



