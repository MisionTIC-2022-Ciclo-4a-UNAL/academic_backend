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

from models.course import Course
from models.enrollment import Enrollment
from models.student import Student
from repositories.enrollment_repository import EnrollmentRepository
from repositories.course_repository import CourseRepository
from repositories.student_repository import StudentRepository

class EnrollmentController:
    def __init__(self):
        print("Enrollment controller ready")
        self.enrollment_repository = EnrollmentRepository()
        self.course_repository = CourseRepository()
        self.student_repository = StudentRepository()

    def index(self) -> list:
        """

        :return:
        """
        return self.enrollment_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.enrollment_repository.find_by_id(id_)

    def get_by_course(self, course_id: str) -> list:
        """

        :param course_id:
        :return:
        """
        return self.enrollment_repository.get_students_in_course(course_id)

    def create(self, enrollment_: dict, course_id: str, student_id: str) -> dict:
        """

        :param student_id:
        :param course_id:
        :param enrollment_:
        :return:
        """
        enrollment = Enrollment(enrollment_)
        course_dict = self.course_repository.find_by_id(course_id)
        course_obj = Course(course_dict)
        student_dict = self.student_repository.find_by_id(student_id)
        student_obj = Student(student_dict)
        enrollment.course = course_obj
        enrollment.student = student_obj
        return self.enrollment_repository.save(enrollment)

    def update(self, id_: str, enrollment_: dict) -> dict:
        """

        :param id_:
        :param enrollment_:
        :return:
        """
        enrollment = Enrollment(enrollment_)
        return self.enrollment_repository.update(id_, enrollment)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.enrollment_repository.delete(id_)
