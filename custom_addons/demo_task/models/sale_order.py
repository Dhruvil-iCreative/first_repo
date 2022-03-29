from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "sale.order"

    def cron_demo_method(self):
        for rec in self:
            if rec.state == "draft":
                rec.state = "sent"
