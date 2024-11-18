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
        'security/ir.model.access.csv',  # Control de permisos
        'views/menu_items.xml',          # Menús para el módulo
        'views/actions.xml',             # Acciones vinculadas al wizard
        'views/views.xml',               # Vista del wizard
        'report/sales_report_templates.xml', # Plantillas del reporte PDF
        'report/sales_report_actions.xml',   # Acciones del reporte PDF
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}

