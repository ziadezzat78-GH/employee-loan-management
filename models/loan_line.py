from odoo import api, fields, models

class LoanLine(models.Model):
    _name = 'employee.loan.line'
    _description = ' Loan Installment'

    loan_id = fields.Many2one('employee.loan',string='Loan')
    amount = fields.Float(string='Amount')
    due_date = fields.Date(string='Due Date')
    state = fields.Selection([('pending', 'Pending'),
                              ('paid', 'Paid'),],default='pending')
