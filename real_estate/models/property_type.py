from odoo import fields, models

class RealEstatePropertyType(models.Model):
    _name = "real.estate.property.type"
    _description = "Real Estate Property Type"
    _order = 'id'

    name = fields.Char('Name', required=True, translate=True)