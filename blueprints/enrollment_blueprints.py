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
from controllers.enrollment_controller import EnrollmentController

enrollment_blueprints = Blueprint('enrollment_blueprints', __name__)
enrollment_controller = EnrollmentController()


@enrollment_blueprints.route("/enrollment/all", methods=['GET'])
def get_enrollments():
    response = enrollment_controller.index()
    return response, 200


@enrollment_blueprints.route("/enrollment/<string:id_>", methods=['GET'])
def get_enrollment_by_id(id_):
    response = enrollment_controller.show(id_)
    return response, 200


@enrollment_blueprints.route("/enrollment/insert", methods=['POST'])
def insert_enrollment():
    enrollment = request.get_json()
    response = enrollment_controller.create(enrollment)
    return response, 201


@enrollment_blueprints.route("/enrollment/update/<string:id_>", methods=['PATCH'])
def update_enrollment(id_):
    enrollment = request.get_json()
    response = enrollment_controller.update(id_, enrollment)
    return response, 201


@enrollment_blueprints.route("/enrollment/delete/<string:id_>", methods=['DELETE'])
def delete_enrollment(id_):
    response = enrollment_controller.delete(id_)
    return response, 204
