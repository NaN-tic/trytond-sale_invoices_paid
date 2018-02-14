# This file is part sale_invoices_paid module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
try:
    from trytond.modules.sale_invoices_paid.tests.test_sale_invoices_paid import suite
except ImportError:
    from .test_sale_invoices_paid import suite

__all__ = ['suite']
