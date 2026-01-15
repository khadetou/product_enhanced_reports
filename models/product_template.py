# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.tools import is_html_empty
from odoo.tools.mail import html2plaintext


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
        For backend views (sale order lines), HTML is converted to plain text for proper display.
        For PDF reports, the HTML description is accessed directly from the product to preserve formatting.
        """
        name = self.display_name
        if self.description_sale and not is_html_empty(self.description_sale):
            # Convert HTML to plain text for the sale order line name field
            # This ensures proper display in backend views without raw HTML tags
            # PDF reports access product.description_sale directly to render HTML formatting
            plain_description = html2plaintext(self.description_sale, include_references=False)
            if plain_description:
                name += '\n' + plain_description
        return name

