from odoo import api, fields, models


class StudentProfile(models.Model):
    _name = 'student.profile'

    description = 'Student Profile'

    name = fields.Char("name", help="please enter name")
    dob = fields.Date("DOB")
    age = fields.Integer("Age")
    contact = fields.Char("Contact")
    height = fields.Float("Height")
    weight = fields.Float("Weight")
    email = fields.Char("Email")
    is_active = fields.Boolean(default=False, help="Set active to false to hide the Account Tag without removing it.")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    department = fields.Selection([('be', 'BE'), ('me', 'ME')],
                                  required=True)

    state = fields.Selection([('initial', 'new'), ('pending_approval', 'Pending For Approval'), ('student', 'Student'),
                              ('not_a_student', 'Left')], string='Status', defult='initial')

    note = fields.Char("Note")
    comment = fields.Html("Comment")

    degree_ids = fields.One2many("student.degree", "student_id", "Degree")
    hobbies_ids = fields.Many2many("student.hobbies", "student_hobbies_rel", "stud_id", "hobby_id", string="Hobbies")

    city = fields.Char("City")
    state_id = fields.Many2one("student.state", string="State")

    subjects = fields.Integer(string="Subject")

    fees = fields.Integer(compute="_compute_total_fees" ,store=True)

    @api.depends("subjects")
    def _compute_total_fees(self):
        for record in self:
            record.fees = 150 * record.subjects

    @api.onchange("name")
    def _onchange_partner_name(self):
        self.note = "welcome to collage %s" % self.name

    def send_approval(self):
        self.state = "pending_approval"

    def make_student(self):
        self.state = "student"

    def leave_school(self):
        self.state = "not_a_student"

    def reset(self):
        self.state = "initial"


class StudentState(models.Model):
    _name = 'student.state'

    description = 'Student state'

    name = fields.Char("Name")
    code = fields.Char("code")


# class StudentDegree(models.Model):
#     _name = 'student.degree'
#
#     _description = 'Student Degree'
#
#     student_id = fields.Many2one('student.profile', "Student")
#
#     sequence = fields.Integer("Sequence")
#     name = fields.Char("Name")
#     university = fields.Char("University")
#     percentage = fields.Float("Percentage")
#     grade = fields.Char("Grade")
#     certificate = fields.Binary("Certificate")


class StudentHobbies(models.Model):
    _name = "student.hobbies"

    _description = "Student Hobbies"

    name = fields.Char("Name")
