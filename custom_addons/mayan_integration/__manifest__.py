{
    'name': 'Mayan EDMS Integration',
    'version': '1.0',
    'category': 'Document Management',
    'summary': 'Integration with Mayan EDMS for document processing',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/mayan_document_views.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
