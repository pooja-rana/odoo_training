from datetime import date

from odoo import api, models, fields, _
from odoo.exceptions import ValidationError
from dateutil import relativedelta


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"
    # _rec_name = 'name'
    # _order = 'ref'

    name = fields.Char(string='Name', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date Of Birth')
    ref = fields.Char(string='Reference', tracking=True)
    # if you store compute method data in database you write store=true
    # if you add inverse method  then add this function inverse='_inverse_compute_age'
    age = fields.Integer(string='Age', compute='_compute_age', search='_search_age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male', tracking=True)

    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")
    image = fields.Image(string='Image')

    tags_ids = fields.Many2many('patient.tag', string='Tags')

    parents = fields.Char('Parents')
    marital_status = fields.Selection([('married', 'Married'),
                                       ('single', 'Single')], string="Marital_Status")
    partner_name = fields.Char('Partner Name')

    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for rec in self:
            if rec.date_of_birth and rec.date_of_birth > fields.Date.today():
                raise ValidationError(_("The date_of_birth not accepted !"))

    @api.model
    def create(self, vals):
        # print("odoo mates", vals)
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    # def write(self, vals):
    #     if not self.ref and not vals.get('ref'):
    #         vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
    #     return super(HospitalPatient, self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    # @api.depends('age')
    # def _inverse_compute_age(self):
    #     today = date.today()
    #     for rec in self:
    #         rec.date_of_birth = today - relativedelta.relativedelta(years=rec.age)

    # def name_get(self):
    #     return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]

    # def write(self, vals):
    #     patient = self.env['hospital.patient'].search([('active', '=', 'True')])
    #     current_patient = self.env['hospital.patient'].browse(5).name
    #     print(current_patient)
    #     print(patient)

    @api.ondelete(at_uninstall=False)
    def _check_appointment(self):
        for rec in self:
            if rec.appointment_id:
                raise ValidationError("you can not delete patient with appointment")

    # def _search_age(self, operator, value):
    #     date_of_birth = date.today() - relativedelta.relativedelta(years=value)
    #     start_of_year = date_of_birth.replace(day = '1' , month = '12')
    #     end_of_year = date_of_birth.replace(day='1',month='12')
    #     print("hooiooooidowecbdskc")
    #     return [('date_of_birth', '>=', start_of_year ),('date_of_birth','=>',end_of_year)]

