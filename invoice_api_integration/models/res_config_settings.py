from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_token = fields.Char(config_parameter='invoice_api_integration.invoice_token',string = 'API Invoice Token', help='Necessary for some functionalities in the API view', copy=True, default="41AX4XfWgj8kpQnGGONtjfYcOVV4u5sMWuVjksWb_I5GS89JVL4loH7XAnC2o", store=True)

