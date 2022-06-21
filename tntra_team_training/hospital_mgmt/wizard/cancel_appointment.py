from datetime import date ,timedelta
import datetime
from odoo import api, models, fields
from odoo.exceptions import ValidationError


class AppointmentCancel(models.TransientModel):
    _name = "appointment.cancel"
    _description = "Appointment Cancel"

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment",
                                     domain=[('state', '=', 'draft'), ('priority', 'in', ['0', '1'])])
    reason = fields.Text(string="Reason")
    cancel_date = fields.Date("Cancel_Date")

    @api.model
    def default_get(self, fields):
        res = super(AppointmentCancel, self).default_get(fields)
        res['cancel_date'] = datetime.date.today()
        return res

    def action_cancel(self):
        allowed_date = self.appointment_id.date_appointment - timedelta(days=3)
        if allowed_date < date.today():
            raise ValidationError("sorry you are cancel appointment ")
        self.appointment_id.state = 'cancel'
