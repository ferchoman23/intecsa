# -*- coding: utf-8 -*-
from odoo import api, models, fields
#from odoo.addons.num_to_words.models.numero_letras import numero_a_letras, numero_a_moneda
import logging, datetime

class ReportCotizacion(models.AbstractModel):
    _name = 'report.intecsa.cotizacion_sale_order'

    def a_letras(self,monto):
        letras = numero_a_moneda(monto)
        return letras
        
    def convertir_fecha_hora(self, fecha_hora):
    	fecha = datetime.datetime.strptime(str(fecha_hora), '%Y-%m-%d %H:%M:%S').date().strftime('%Y-%m-%d')
    	hora = datetime.datetime.strftime(fields.Datetime.context_timestamp(self, datetime.datetime.now()), "%H:%M:%S")
    	logging.warning("funcion")
    	informacion = {
    		'fecha': fecha,
    		'hora': hora,
    	}
    	return informacion

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        logging.warning("hola")
        return {
            'convertir_fecha_hora': self.convertir_fecha_hora,
            'doc_ids': docids,
            'doc_model': 'stock.picking',
            'docs': docs,
            #'a_letras': self.a_letras,

        }
