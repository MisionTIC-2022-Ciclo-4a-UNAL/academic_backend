"""
 # Copyright: Copyright (c) 2022
 #
 # License
 #
 # Copyright (c) 2022 by Carlos Andres Sierra Virgüez.
 # All rights reserved.
 #
 # This file is part of Academic #MisionTIC2022 Project Software.
 #
 # Academic #MisionTIC2022 Project is free software: you can redistribute it and/or modify it
 # under the terms of the GNU General Public License as published by the Free Software Foundation,
 # either version 3 of the License, or (at your option) any later version.
 #
 # Academic #MisionTIC2022 Project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 # without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 # See the GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License along with Academic #MisionTIC2022 Project.
 # If not, see <https://www.gnu.org/licenses/>.
"""

from flask import Blueprint, request
from controllers.department_controller import DepartmentController

department_blueprints = Blueprint('department_blueprints', __name__)
department_controller = DepartmentController()


@department_blueprints.route("/department/all", methods=['GET'])
def get_departments():
    response = department_controller.index()
    return response, 200


@department_blueprints.route("/department/<string:id_>", methods=['GET'])
def get_department_by_id(id_):
    response = department_controller.show(id_)
    return response, 200


@department_blueprints.route("/department/insert", methods=['POST'])
def insert_department():
    department = request.get_json()
    response = department_controller.create(department)
    return response, 201


@department_blueprints.route("/department/update/<string:id_>", methods=['PATCH'])
def update_department(id_):
    department = request.get_json()
    response = department_controller.update(id_, department)
    return response, 201


@department_blueprints.route("/department/delete/<string:id_>", methods=['DELETE'])
def delete_department(id_):
    response = department_controller.delete(id_)
    return response, 204
