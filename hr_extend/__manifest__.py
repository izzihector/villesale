# -*- encoding: utf-8 -*-


{
    'name': u'Commune de Salé: Gestion des Ressources Humaines',
    'version': '1.0',
    'summary': u'RH',
    'author': 'Osisoftware',
    'website': '',
    "depends": [
        'hr', 'hr_contract'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_position_views.xml',
        'views/hr_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
