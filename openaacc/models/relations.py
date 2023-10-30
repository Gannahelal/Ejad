from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MainModel(models.Model):
    _name = 'openaacc.main_model'

    name = fields.Char(string='Name')
    child_ids = fields.One2many('openaacc.child_model', 'parent_id', string='Children')

    # @api.constrains('child_ids')
    def action_confirm(self):
        for rec in self:
            childs = self.env['openacc.child_model'].search([])
            print("patients........", childs)

        # for record in self:
        #     chid = self.child_ids.create({'name': record.child_ids.name})
        #     chid_wr = self.child_ids.write({'name': record.child_ids.name})
        #     child_sr = self.child_ids.search([('name', 'in', record.child_ids.name)])
        #     print(chid)
        #     print(chid_wr)
        #     print(child_sr)
        #     if len(record.child_ids) > 5:
        #         raise ValidationError("Cannot have more than 5 child records.")


class ChildModel(models.Model):
    _name = 'openaacc.child_model'

    name = fields.Char(string='Name')
    parent_id = fields.Many2one('openaacc.main_model', string='Parent')
