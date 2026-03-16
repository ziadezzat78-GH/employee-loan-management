# Employee Loan Management - Odoo 18

A professional Odoo 18 module for managing employee loan requests, approvals, installment tracking, and payroll integration.

## Features

- Employee loan requests with approval workflow
- Auto-generated loan reference (LOAN/YYYY/XXXX)
- Multi-level approval (Employee → Manager)
- Automatic installment generation on approval
- Computed fields (Amount Paid / Amount Remaining)
- Kanban view for visual loan management
- Search filters and Group By options
- Email notifications on approval/rejection
- PDF Loan Agreement report
- Payroll integration (auto-deduct installments from salary)
- Chatter with full activity tracking

## Installation

1. Copy the `employee_loan` folder to your Odoo addons path
2. Update your `odoo.conf` to include the addons path
3. Restart Odoo server
4. Go to Apps → Update Apps List
5. Search for "Employee Loan Management" and install

## Technical Details

- **Odoo Version:** 18.0 Enterprise
- **Models:** `employee.loan`, `employee.loan.line`
- **Dependencies:** `hr`, `hr_payroll`, `mail`

## Workflow

Draft → Confirmed → Approved → Rejected

## Author

Ziad Waleed - Junior Odoo Developer
