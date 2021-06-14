# -*- encoding: utf-8 -*-


{
    'name': u'Commune de Salé: Gestion de la Fourrière',
    'version': '1.0',
    'summary': u'Gestion de Fourrière pour la ville de Salé',
    'author': 'Osisoftware',
    'website': '',
    "depends": [
        'mail', 'project_extend'
    ],
    'data': [
        'data/data.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        # 'report/docs_admin_templates.xml',
        # 'report/report.xml',
        'views/fourriere_views.xml',
        'views/config_views.xml',
        'wizard/quitance_wizard.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
