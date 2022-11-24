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
from controllers.course_controller import CourseController

course_blueprints = Blueprint('course_blueprints', __name__)
course_controller = CourseController()


@course_blueprints.route("/course/all", methods=['GET'])
def get_courses():
    response = course_controller.index()
    return response, 200


@course_blueprints.route("/course/<string:id_>", methods=['GET'])
def get_course_by_id(id_):
    response = course_controller.show(id_)
    return response, 200


@course_blueprints.route("/course/insert", methods=['POST'])
def insert_course():
    course = request.get_json()
    response = course_controller.create(course)
    return response, 201


@course_blueprints.route("/course/update/<string:id_>", methods=['PATCH'])
def update_course(id_):
    course = request.get_json()
    response = course_controller.update(id_, course)
    return response, 201


@course_blueprints.route("/course/delete/<string:id_>", methods=['DELETE'])
def delete_course(id_):
    response = course_controller.delete(id_)
    return response, 204
