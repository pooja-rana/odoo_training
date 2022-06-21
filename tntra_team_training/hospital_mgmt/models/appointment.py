from odoo import api, models, fields
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient', ondelete='restrict') # also use ondelete=cascade
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, related='patient_id.gender')
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    ref = fields.Char(string='Reference', help=" Reference of the patient of patient Detail")
    prescription = fields.Html(string='Prescription')
    pharmacy_line_ids = fields.One2many('appointment.prescription.lines', 'appointment_id',
                                        string="Prescription Lines")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority",
        help='Gives the sequence order when displaying a list of MRP documents.')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string='status', default='draft')

    doctor_id = fields.Many2one('res.users', string='Doctor')
    hide_sales_price = fields.Boolean(string='hide sales price')

    def action_in_consultation(self):
        self.state = 'in_consultation'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        # self.state = 'cancel'
        action = self.env.ref("hospital_mgmt.action_cancel_appointment_view").read()[0]
        return action

    def action_draft(self):
        self.state = 'draft'

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    @api.constrains('date_appointment')
    def _check_date_end(self):
        for record in self:
            if record.date_appointment < fields.Date.today():
                raise ValidationError("The appointment date cannot be set in the past")

    def unlink(self):
        if self.state == 'done':
            raise ValidationError("You Cannot Delete as it is in Done State")
        return super(HospitalAppointment, self).unlink()

    def action_test(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': "action successfully",
                'type': 'rainbow_man',
            }
        }


class AppointmentPrescriptionLines(models.Model):
    _name = "appointment.prescription.lines"
    _description = "Appointment Prescription Lines"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float('Price')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    doctor_signature = fields.Binary('DoctorSignature')
