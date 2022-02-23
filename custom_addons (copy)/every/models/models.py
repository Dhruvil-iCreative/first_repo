# -*- coding: utf-8 -*-

from odoo import models, fields, api


class every(models.Model):
    _name = 'every.every'
    _inherit='hospital.hospital'
    _description = 'every.every'

    t_doc = fields.Char(string="Treatment Doctor")
    t_doc_number = fields.Char(string="Contact Number")
    t_doc_exp = fields.Integer(string="Experience")
    t_doc_qua = fields.Char(compute="_value_pc",store=True,string="Level of Doctor")

    @api.depends('t_doc_exp')
    def _value_pc(self):
        for record in self:
            if record.t_doc_exp<=1:
                record.t_doc_qua="Beginner"
            elif 1<record.t_doc_exp<5:
                record.t_doc_qua="Medium"
            else:
                record.t_doc_qua="Advance"
