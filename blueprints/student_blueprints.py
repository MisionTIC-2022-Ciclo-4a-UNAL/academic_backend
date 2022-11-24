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
from controllers.student_controller import StudentController

student_blueprints = Blueprint('student_blueprints', __name__)
student_controller = StudentController()


@student_blueprints.route("/student/all", methods=['GET'])
def get_students():
    response = student_controller.index()
    return response, 200


@student_blueprints.route("/student/<string:id_>", methods=['GET'])
def get_student_by_id(id_):
    response = student_controller.show(id_)
    return response, 200


@student_blueprints.route("/student/insert", methods=['POST'])
def insert_student():
    student = request.get_json()
    response = student_controller.create(student)
    return response, 201


@student_blueprints.route("/student/update/<string:id_>", methods=['PATCH'])
def update_student(id_):
    student = request.get_json()
    response = student_controller.update(id_, student)
    return response, 201


@student_blueprints.route("/student/delete/<string:id_>", methods=['DELETE'])
def delete_student(id_):
    response = student_controller.delete(id_)
    return response, 204
