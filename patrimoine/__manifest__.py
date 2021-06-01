# -*- encoding: utf-8 -*-


{
    'name': u'Commune de Salé: Gestion des Loyers',
    'version': '1.0',
    'summary': u'Loyers',
    'author': 'Osisoftware',
    'website': '',
    "depends": [
        'project_extend', 'web_google_maps', 'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/patrimoine_views.xml',
        'views/patrimoine_loyer_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
