# Copyright 2023 Karthik <karthik@sodexis.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    company_ids = fields.Many2many(
        comodel_name="res.company",
        column1="product_id",
        column2="company_id",
        relation="product_product_company_rel",
        related="product_tmpl_id.company_ids",
        compute_sudo=True,
        readonly=False,
        store=True,
    )
