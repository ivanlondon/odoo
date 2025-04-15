{
    'name': 'Juvana Theme',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Juvana Custom Backend Theme',
    'sequence': 1,
    'website': 'https://www.juvana.ai',
    'description': """
        Custom backend theme for Juvana using brand colors and styling
    """,
    'author': 'Juvana',
    'depends': [
        'web',
        'base',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'juvana_theme/static/src/scss/style.scss',
            'juvana_theme/static/src/js/theme.js',
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
