from odoo import fields, models


class StudentDegree(models.Model):
    _name = 'student.degree'

    _description = 'Student Degree'

    student_id = fields.Many2one('student.profile', "Student")

    sequence = fields.Integer("Sequence")
    degree = fields.Char("degree")
    gender = fields.Selection(related='student_id.gender')
    university = fields.Char("University")
    percentage = fields.Float("Percentage")
    grade = fields.Char("Grade")
    certificate = fields.Binary("Certificate")
