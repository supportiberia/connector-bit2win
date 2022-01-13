# coding: utf-8
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2020 Rapsodoo Iberia
#    (<http://www.rapsodoo.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Bit2win Connector',
    'version': '15.0.0.0.1',
    'summary': """Bit2win on Odoo""",
    'description': """Bit2win on Odoo: Quotations, Sales, Products, ...""",
    'license': 'AGPL-3',
    'author': "Rapsodoo Iberia",
    'website': "https://www.rapsodoo.com/es/",
    'depends': ['base', 'mail', 'web', 'sale', 'sale_management'],
    'data': [
        'views/views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'https://bit2win-webc-run-main-cbgqfdnwxa-ew.a.run.app/elements/b2w-base.js',
            'https://bit2win-webc-run-main-cbgqfdnwxa-ew.a.run.app/elements/b2w-catalogs.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}