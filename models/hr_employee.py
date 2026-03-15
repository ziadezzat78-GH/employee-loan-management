from odoo import models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def _get_loan_deduction(self):
        loans = self.env['employee.loan'].search([
            ('employee_id', '=', self.id),
            ('state', '=', 'approved'),
        ])
        total_deduction = 0
        for loan in loans:
            installment = loan.loan_line_ids.filtered(
                lambda l: l.state == 'pending'
            )
            if installment:
                installment = installment[0]
                total_deduction += installment.amount
                installment.state = 'paid'
        return total_deduction