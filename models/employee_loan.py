from email.policy import default

from odoo import models, fields , api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class EmployeeLoan(models.Model):
    _name = 'employee.loan'
    _description = 'Employee Loan'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Loan Reference', default='New', copy=False)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    amount = fields.Float(string='Loan Amount', required=True)
    installments = fields.Integer(string='Number of Installments', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft',tracking=True)
    notes = fields.Text(string='Notes')
    loan_line_ids = fields.One2many('employee.loan.line', 'loan_id', string='Installments')
    amount_paid = fields.Float(string='Amount Paid', compute='_compute_amounts')
    amount_remaining = fields.Float(string='Amount Remaining', compute='_compute_amounts')

    @api.constrains('amount')
    def check_amount(self):
        for rec in self:
            if rec.amount > 10000:
                raise ValidationError(
                    "installment cannot be more than than 10000")
            elif rec.amount < 1000:
                raise ValidationError("installment cannot be less than 1000")




    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirmed'

    def action_approve(self):
        self.state = 'approved'
        installment_amount = self.amount / self.installments
        for i in range(1, self.installments + 1):
            self.env['employee.loan.line'].create({
                'loan_id': self.id,
                'amount': installment_amount,
                'due_date': fields.Date.today() + relativedelta(months=i),
                'state': 'pending',
            })
        template = self.env.ref('employee_loan.email_template_loan_approved')
        template.send_mail(self.id, force_send=True)

    def action_reject(self):
        self.state = 'rejected'
        template = self.env.ref('employee_loan.email_template_loan_rejected')
        template.send_mail(self.id, force_send=True)

    @api.model_create_multi
    def create(self, vals_list):
     for vals in vals_list:
         if vals.get('name', 'New') == 'New':
               vals['name'] = self.env['ir.sequence'].next_by_code('employee.loan')
     return super(EmployeeLoan, self).create(vals_list)

    @api.depends('loan_line_ids.state', 'loan_line_ids.amount')
    def _compute_amounts(self):
        for rec in self:
            paid_lines=rec.loan_line_ids.filtered(lambda l: l.state == 'paid')
            rec.amount_paid=sum(paid_lines.mapped('amount'))
            rec.amount_remaining = rec.amount - rec.amount_paid

