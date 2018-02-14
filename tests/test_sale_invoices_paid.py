# This file is part of the sale_invoices_paid module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleInvoicesPaidTestCase(ModuleTestCase):
    'Test Sale Invoices Paid module'
    module = 'sale_invoices_paid'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleInvoicesPaidTestCase))
    return suite
