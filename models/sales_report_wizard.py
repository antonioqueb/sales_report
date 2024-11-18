# -*- coding: utf-8 -*-
# Modelo Transient para el Wizard del reporte simplificado de ventas
from odoo import models, fields, api

class SalesReportWizard(models.TransientModel):
    _name = 'sale.report.wizard'
    _description = 'Wizard para generar reporte de ventas'

    # Campos del formulario
    start_date = fields.Date(string='Fecha Inicio', required=True)
    end_date = fields.Date(string='Fecha Fin', required=True)

    # Acción para generar el reporte
    def action_generate_report(self):
        data = {
            'model': self._name,
            'form': {
                'start_date': self.start_date,
                'end_date': self.end_date,
            },
        }
        return self.env.ref('simplified_sales_report.action_sales_report_pdf').report_action(self, data=data)

