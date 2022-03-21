from odoo import models, fields, api
from datetime import date


class ContactImprove(models.Model):
    _inherit = ["res.partner"]

    birth_date = fields.Date(default=date.today())
    age = fields.Integer(compute="_compute_age")
    today_date = fields.Date(default=date.today())

    def name_get(self):
        result = []
        for rec in self:

            result.append((rec.id, f"{rec.name} - {rec.  phone}"))
            print(result)
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = ['|', ('email', operator, name), ('city', operator, name)]
        return super(ContactImprove, self)._name_search(name, args=args+domain, operator=operator, limit=limit, name_get_uid=name_get_uid)

    @api.depends("birth_date", "today_date")
    def _compute_age(self):
        if self.birth_date:
            self.age = self.today_date.year - self.birth_date.year
        else:
            self.age = 0
