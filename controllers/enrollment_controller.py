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

from models.enrollment import Enrollment
from repositories.enrollment_repository import EnrollmentRepository


# TODO check validations and errors codes
class EnrollmentController:

    def __init__(self):
        """
        This is the constructor of the EnrollmentController class
        """
        print("Enrollment controller ready")
        self.enrollment_repository = EnrollmentRepository()

    # Equivalent to 'all'
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

    def create(self, enrollment_: dict) -> dict:
        """

        :param enrollment_:
        :return:
        """
        enrollment = Enrollment(enrollment_)
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
