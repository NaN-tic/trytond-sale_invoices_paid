#This file is part sale_invoices_paid module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'
    invoices_paid = fields.Function(fields.Boolean('Paid', select=True),
        'get_invoices_paid')

    @classmethod
    def get_invoices_paid(cls, records, name):
        """Get invoices are paid"""
        result = {}
        paid = False
        invoice_paid = []
        for sale in records:
            if sale.invoices:
                for invoice in sale.invoices:
                    if invoice.state == 'paid':
                        invoice_paid.append(invoice.id)
                if len(invoice_paid) == len(sale.invoices):
                    paid = True
            result[sale.id] = paid
        return result
