{
    'name': 'Tutoriales de Inventario',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Tutoriales para aprender a trabajar con el módulo de inventario',
    'description': """
        Este módulo proporciona tutoriales interactivos para aprender
        a trabajar con el módulo de inventario de Odoo.
    """,
    'author': 'Tu Empresa',
    'depends': ['stock', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_tutorial_views.xml',
        'views/tutorial_wizard_views.xml',
        'views/menu_views.xml',
        'data/tutorial_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}