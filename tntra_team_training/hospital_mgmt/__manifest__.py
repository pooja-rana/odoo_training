
{
    'name' : 'Hospital Management',
    'version' : '1.2',
    'author' : 'Pooja Rana',
    'maintainer': ['Tntra'],
    'sequence':-100,
    'website' : 'https://www.tntra.io',
    'depends' : ['base','mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/sequence_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment.xml',
        'views/menu_view.xml',
        'views/patient_view.xml',
        'views/appointment.xml',
        'views/patient_tag_view.xml',
        'views/operation_view.xml',
        ],
    'application': True,
    'auto_install': False,
}
