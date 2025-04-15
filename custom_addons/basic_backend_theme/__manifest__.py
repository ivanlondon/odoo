{
    'name': 'Basic Backend Theme',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Clean and Modern Backend Theme',
    'sequence': 1,
    'website': 'https://www.example.com',
    'description': """
        Simple and clean backend theme for Odoo 16.0 Community Edition
    """,
    'author': 'Ivan London',
    'depends': [
        'web',
        'base',
    ],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'basic_backend_theme/static/src/scss/style.scss',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
