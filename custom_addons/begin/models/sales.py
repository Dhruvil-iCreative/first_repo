# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mobile = fields.Char()
    email = fields.Char()

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        for rec in self:
            rec.mobile = rec.partner_id.phone
            rec.email = rec.partner_id.email

    @api.constrains('payment_term_id', 'partner_id')
    def _check_payment_term(self):
        for rec in self:
            if rec.payment_term_id != rec.partner_id.property_supplier_payment_term_id:
                raise UserError('Payment Terms do not match!')

    def default_wiz(self):
        return self.env['ir.actions.act_window']._for_xml_id("begin.sale_order_default_wiz_views_action_window")

