from odoo import models, fields, api

class InventoryTutorial(models.Model):
    _name = 'inventory.tutorial'
    _description = 'Tutorial de Inventario'
    _order = 'sequence, id'

    name = fields.Char('Título del Tutorial', required=True)
    sequence = fields.Integer('Secuencia', default=10)
    description = fields.Text('Descripción')
    content = fields.Html('Contenido del Tutorial')
    gif_guide = fields.Binary('GIF Guiado', help='GIF animado que muestra los pasos del tutorial')
    gif_filename = fields.Char('Nombre del GIF')
    category = fields.Selection([
        ('basic', 'Conceptos Básicos'),
        ('operations', 'Operaciones'),
        ('reports', 'Reportes'),
        ('advanced', 'Avanzado')
    ], string='Categoría', default='basic')
    active = fields.Boolean('Activo', default=True)
    
    def action_view_tutorial(self):
        return {
            'type': 'ir.actions.act_window',
            'name': self.name,
            'res_model': 'inventory.tutorial',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('inventory_tutorials.view_tutorial_wizard').id,
            'target': 'new',
        }