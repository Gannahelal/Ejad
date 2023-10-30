# -*- coding: utf-8 -*-

from odoo import models, fields,api
from odoo.tools.translate import _


class HospitalPatient(models.Model):
    _name = 'openacc.patient'
    _description = 'patient record'
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is Child ?")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    date_field = fields.Date(string='Date Field')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status", tracking=True)
    datetime_field = fields.Datetime(string='Datetime Field')
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")

    def action_create(self):

        HOSPITAL = self.env['hospital.appointment']
        H = HOSPITAL.browse(10)
        print('obj: ', H)
        self.write({"appointment_ids": [
            (1, H.id, {"name": "app1"})
        ]})
    def action_unlink(self):
        self.write({"appointment_ids":[(3,10)]})
raise Warning(_('This is the warning message to translate.'))



