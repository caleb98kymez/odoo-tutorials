from odoo import fields, models

class PropertyTag(models.Model):
    _name = 'real.estate.property.tag'
    _description = 'Real Estate Property Tag'
    _order = 'id'

    name = fields.Char('Name', required=True, translate=True)