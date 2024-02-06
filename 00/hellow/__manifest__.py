##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2018 Marlon Falcon Hernandez
#    (<http://www.marlonfalcon.com>).
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
    'name': 'Mascotas',
    'version': '16.0.1.0.0',
    'author': 'Victor Carrion',
    'maintainer': 'Victor Carrion',
    'website': 'http://www.vr.com',
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'summary': 'Hola Mundo, probando la creacion de un primer modulo para Odoo.',
    'depends': ['base'],
    'data': [
              'security/ir.model.access.csv',  
              #'data/pet_data.xml',   
              'views/views.xml',
            ],
    'images': ['static/description/icon.jpg'],
}
