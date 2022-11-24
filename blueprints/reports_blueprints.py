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

from flask import Blueprint
from controllers.reports_controller import ReportsController

reports_blueprints = Blueprint('reports_blueprints', __name__)
reports_controller = ReportsController()


@reports_blueprints.route("/reports/student_enrollments/all", methods=['GET'])
def report_students_enrollments():
    response = reports_controller.report_students_enrollments()
    return response, 200


@reports_blueprints.route("/reports/student_enrollments/<string:id_>", methods=['GET'])
def report_students_enrollments_by_id(id_: str):
    response = reports_controller.report_students_enrollments(id_)
    return response, 200


@reports_blueprints.route("/reports/course_enrollments/all", methods=['GET'])
def report_course_enrollments():
    response = reports_controller.report_course_enrollments()
    return response, 200


@reports_blueprints.route("/reports/course_enrollments/<string:id_>", methods=['GET'])
def report_course_enrollments_by_id(id_: str):
    response = reports_controller.report_course_enrollments(id_)
    return response, 200


@reports_blueprints.route("/reports/students_top_enrollments", methods=['GET'])
def report_students_more_enrollments():
    response = reports_controller.report_students_more_enrollments()
    return response, 200


@reports_blueprints.route("/reports/department_enrollments", methods=['GET'])
def report_department_enrollments():
    response = reports_controller.report_department_enrollments()
    return response, 200


@reports_blueprints.route("/reports/department_distribution", methods=['GET'])
def report_department_distribution():
    response = reports_controller.report_department_distribution()
    return response, 200
