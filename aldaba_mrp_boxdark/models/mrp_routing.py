from odoo import models, fields, api, _


class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    routing_id = fields.Many2one('mrp.routing', 'Parent Routing', index=True, ondelete='cascade', required=True)


class MrpRouting(models.Model):
    _inherit = 'mrp.routing.workcenter'

    routing_id = fields.Many2one('mrp.routing', 'Parent Routing')

    @api.model
    def create(self, vals_list):
        res = super(MrpRouting, self).create(vals_list)
        if res.bom_id:
            routing_id = res.bom_id.mapped('routing_id')
            list_worker = [item.id for item in [item for item in routing_id.mapped('operation_ids')]]
            list_worker.append(res.id)
            routing_id.write({'operation_ids': list_worker})
        return res


class MrpRoutingOld(models.Model):
    _name = 'mrp.routing'
    _description = 'Routings'

    name = fields.Char('Routing', required=True)
    active = fields.Boolean('Active', default=True,
                            help="If the active field is set to False, it will allow you to hide the routing without "
                                 "removing it.")
    code = fields.Char('Reference', copy=False, default=lambda self: _('New'), readonly=True)
    note = fields.Text('Description')
    operation_ids = fields.One2many('mrp.routing.workcenter', 'routing_id', 'Operations', copy=True)
    location_id = fields.Many2one('stock.location', 'Raw Materials Location',
                                  help="Keep empty if you produce at the location where you find the raw materials. "
                                       "Set a location if you produce at a fixed location. This can be a partner "
                                       "location if you subcontract the manufacturing operations.")
    company_id = fields.Many2one('res.company', 'Company',
                                 default=lambda self: self.env['res.company']._company_default_get('mrp.routing'))

    @api.model
    def create(self, vals):
        if 'code' not in vals or vals['code'] == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('mrp.routing') or _('New')
        return super(MrpRoutingOld, self).create(vals)
