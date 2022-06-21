from odoo import api, models, fields


class PatientOperation(models.Model):
    _name = "patient.operation"
    _description = "Patient Operation"
    _rec_name = 'operation_name'

    doctor_id = fields.Many2one('res.users', string='Doctor')
    operation_name = fields.Char(string='Operation', tracking=True)
    reference_record = fields.Reference(selection=[('hospital.patient', 'Patient'),
                                                   ('hospital.appointment', 'Appointment')], string="Record")
