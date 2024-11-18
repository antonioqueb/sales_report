# -*- coding: utf-8 -*-
{
    'name': 'Simplified Sales Report',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Genera reportes simplificados de ventas.',
    'description': 'Este módulo permite generar reportes simplificados de ventas filtrados por rango de fechas.',
    'author': 'Alpha',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/sales_report_templates.xml',
        'report/sales_report_actions.xml',
        ],

    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}

