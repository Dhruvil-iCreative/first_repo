# -*- coding: utf-8 -*-

from odoo import models, fields, api


class begin(models.Model):
    _name = 'begin.begin'
    _description = 'begin.begin'
    id = fields.Integer()
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    uids = fields.One2many("sale.order", "uids", string="User_ids")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
