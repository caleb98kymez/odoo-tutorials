"""Tutorial to get the models in the real estate app."""
from odoo import fields, models, api


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _order = 'id'

    name = fields.Char('Title', required=True, translate=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', copy=False, default=fields.Date.today().replace(month=fields.Date.today().month + 3))
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)', required=True)
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], 'Garden Orientation')
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('cancelled', 'Cancelled')],
        required=True, copy=False, default='new'
    )
    property_type_id = fields.Many2one('real.estate.property.type', string='Property Type')
    buyer_id = fields.Many2one('res.partner', string='Buyer', index=True, copy=False)
    salesman_id = fields.Many2one('res.users', string='Salesman', index=True, default=lambda self: self.env.user)
    tags_id = fields.Many2many('real.estate.property.tag', string='Tags')
    offer_ids = fields.One2many('real.estate.property.offer', 'property_id', string='Offers')
    total_area = fields.Integer('Total Area (sqm)', compute='_compute_total_area')
    best_price = fields.Float('Best Price', compute='_compute_best_price')

    @api.depends('living_area', 'garden_area', 'offer_ids')
    def _compute_total_area(self):
        for property in self:
            property.total_area = property.living_area + property.garden_area

    def _compute_best_price(self):
        for property in self:
            property.best_price = max(property.offer_ids.mapped('price')) if property.offer_ids else 0
