# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Product Enhanced Reports',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Enhance product display in reports with bold names and HTML descriptions',
    'description': """
Product Enhanced Reports
========================

This module enhances product display in sales reports by:

1. **Bold Product Names**: Product names appear in bold font weight in all 
   sales reports (quotations, orders, invoices) to better distinguish them 
   from descriptions.

2. **HTML Editor for Product Descriptions**: 
   - Enables HTML editor for the product description field (description_sale)
   - Allows rich text formatting: bullet points, bold, italics, etc.
   - Similar to the HTML editing experience in quotation "Conditions générales"
   - HTML content renders properly in PDF reports

This improves readability and presentation quality in all sales documents.
    """,
    'author': 'Custom Development',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'product',
        'sale',
        'account',
    ],
    'data': [
        'views/product_template_views.xml',
        'report/sale_report_templates.xml',
        'report/account_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

