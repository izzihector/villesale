# -*- encoding: utf-8 -*-


{
    'name': u'Checklist par étape de projet',
    'version': '1.0',
    'summary': u'',
    'author': 'Osisoftware',
    'website': '',
    "depends": [
        'project'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_task_type_views.xml',
        'views/project_task_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
