# Copyright 2022-TODAY Rapsodoo Iberia S.r.L. (www.rapsodoo.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': "Aldaba: MRP Box Dark",
    'summary': 'Connecting MRP with the old API model',
    'author': "Rapsodoo Iberia",
    'website': "https://www.rapsodoo.com/es/",
    'category': 'MRP/MRP',
    'license': 'LGPL-3',
    'version': '15.0.1.0.1',
    'depends': ['base', 'stock', 'mrp', 'mrp_workorder'],
    'data': [
        'data/aldaba_data.xml',
        'security/ir.model.access.csv',
        'views/mrp_routing.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
