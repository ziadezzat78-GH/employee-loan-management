{
    'name': 'Employee Loan Management',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Manage employee loans and deductions',
    'description': """
        This module allows employees to request loans,
        managers to approve or reject them,
        and automatically deducts installments from payroll.
    """,
    'author': 'Ziad',
    'depends': ['hr', 'hr_payroll','mail'],
    'data': ['security/res_groups.xml',
        'security/ir.model.access.csv',
             'data/loan_sequence.xml',
             'data/mail_templates.xml',
             'data/hr_payroll_data.xml',
             'views/employee_loan_views.xml',
             'report/employee_loan_report.xml',
             'report/employee_loan_report_template.xml',
             ],
    'installable': True,
    'application': True,
}