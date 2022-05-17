from odoo import fields, models


class StudentDegree(models.Model):
    _name = 'student.degree'

    _description = 'Student Degree'

    student_id = fields.Many2one('student.profile', "Student")

    sequence = fields.Integer("Sequence")
    name = fields.Char("Name")
    university = fields.Char("University")
    percentage = fields.Float("Percentage")
    grade = fields.Char("Grade")
    certificate = fields.Binary("Certificate")
