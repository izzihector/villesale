# -*- encoding: utf-8 -*-


{
    'name': u'Commune de Salé: Gestion de Projets',
    'version': '1.0',
    'summary': u'Projets',
    'author': 'Osisoftware',
    'website': '',
    "depends": [
        'project',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'views/project_views.xml',
        'views/task_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
