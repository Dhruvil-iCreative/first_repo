from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.hospital'
    _description = 'hospital.hospital'

    fname = fields.Char()
    lname=fields.Char()
    image=fields.Binary()
    mobile=fields.Char()
    email=fields.Char()
    gender=fields.Selection([('m',"Male"),("f","Female"),("o","Other")])
    city=fields.Selection([("a","Ahmedabad"),("b","Baroda"),("r","Rajkot"),("s","Surat")])
    reason = fields.Text()
    disease=fields.Selection([("d","Dangue"),("v","Viral"),("m","Maleria"),("d","Diarhea")])
    visit_fee = fields.Integer()
    medication_fee=fields.Integer()
    total_fee = fields.Float(compute="_value_pc", store=True)
    treatement_mode=fields.Selection([('o',"Operation"),("s","Surgery"),("m","Medicines")])
    treatement_cost=fields.Float()
    treatement_date=fields.Date()
    treatement_disc=fields.Char()
    rec_opt=fields.Selection([("y","Yes"),("n","No")],string="Recommendation Option")
    rec_hos=fields.Char(string="Recommended Hospital")
    rec_doc=fields.Char(string="Doctor name")

    @api.depends('visit_fee','medication_fee')
    def _value_pc(self):
        for record in self:
            record.total_fee = float(record.visit_fee) + float(record.medication_fee)



