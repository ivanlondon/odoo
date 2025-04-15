from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mayan_url = fields.Char(string='Mayan EDMS URL', config_parameter='mayan_integration.url')
    mayan_api_token = fields.Char(string='Mayan API Token', config_parameter='mayan_integration.api_token')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            mayan_url=ICPSudo.get_param('mayan_integration.url'),
            mayan_api_token=ICPSudo.get_param('mayan_integration.api_token'),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param('mayan_integration.url', self.mayan_url)
        ICPSudo.set_param('mayan_integration.api_token', self.mayan_api_token)
