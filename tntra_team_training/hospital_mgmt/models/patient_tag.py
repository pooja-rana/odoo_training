from odoo import models, fields, api


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string="color")

    _sql_constraints = [
        ('unique_tag_name', 'unique(name)', 'The name must be unique!'),
    ]

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        print("copycopycopy_________________________________")
        if default is None:
            default = {}
        if not default.get('name'):
            default['name'] = self.name
        return super(PatientTag, self).copy(default)
