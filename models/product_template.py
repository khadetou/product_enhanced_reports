# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.tools import is_html_empty


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Override description_sale to use Html field instead of Text
    # This enables the HTML editor widget for rich text formatting
    description_sale = fields.Html(
        string='Sales Description',
        translate=True,
        help="A description of the Product that you want to communicate to your customers. "
             "This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note. "
             "You can use HTML formatting like bullet points, bold, italics, etc."
    )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def get_product_multiline_description_sale(self):
        """Compute a multiline description of this product, in the context of sales.
        
        Overridden to handle HTML content in description_sale field.
        The description is kept as HTML to preserve formatting (bullet points, bold, etc.)
        when rendered in reports.
        """
        name = self.display_name
        if self.description_sale and not is_html_empty(self.description_sale):
            # Keep HTML content - it will be rendered properly in reports
            name += '\n' + self.description_sale
        return name

