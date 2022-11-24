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
from repositories.course_repository import CourseRepository


# TODO check validations and errors codes
class CourseController:

    def __init__(self):
        """
        This is the constructor of the CourseController class
        """
        self.course_repository = CourseRepository()

    def index(self) -> list:
        """

        :return:
        """
        return self.course_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.course_repository.find_by_id(id_)

    def create(self, course_: dict) -> dict:
        """

        :param course_:
        :return:
        """
        course = Course(course_)
        return self.course_repository.save(course)

    def update(self, id_, course_: dict) -> dict:
        """

        :param id_:
        :param course_:
        :return:
        """
        course = Course(course_)
        return self.course_repository.update(id_, course)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.course_repository.delete(id_)
