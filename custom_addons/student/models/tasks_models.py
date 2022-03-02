from odoo import models, fields, api


class tasks(models.Model):
    _name="tasks.tasks"
    _rec_name="task_name"


    task_name=fields.Char(string="Task")
    task_duration=fields.Char(string="Duration")
    task_mem_involve=fields.Integer(string="No of Member")
    task_deadline=fields.Datetime(string="Deadline")
