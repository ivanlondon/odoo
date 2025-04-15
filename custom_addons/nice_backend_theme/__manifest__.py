{
    'name': 'Nice Backend Theme',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Modern and Clean Backend Theme based on NiceAdmin',
    'sequence': 1,
    'website': 'https://www.juvana.ai',
    'description': """
        Modern and responsive backend theme for Odoo 16.0 based on NiceAdmin template.
        Features:
        - Modern dashboard layout
        - Clean and professional design
        - Responsive sidebar
        - Dark/light mode support
        - Custom cards and widgets
    """,
    'author': 'Juvana',
    'depends': [
        'web',
        'base',
    ],
    'data': [
        'views/assets.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'nice_backend_theme/static/src/scss/style.scss',
            'nice_backend_theme/static/src/js/sidebar.js',
            ('nice_backend_theme/static/src/js/theme.js', {
                'type': 'assets',
                'priority': 2
            }),
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
