# -*- coding: utf-8 -*-

from odoo import models, fields, api


class dhruv_page(models.Model):
    _name = 'dhruv_page.dhruv_page'
    _description = 'dhruv_page.dhruv_page'

    name = fields.Char()
    value = fields.Integer()
    # city = fields.Selection([("ahm", 'Ahmedabad'), ("raj", 'Rajkot'), ("sur", 'Surat')])
    city = fields.Selection(
        string='Type',
        selection=[('lead', 'Lead'), ('opportunity', 'Opportunity')],
        help="Type is used to separate Leads and Opportunities")
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
