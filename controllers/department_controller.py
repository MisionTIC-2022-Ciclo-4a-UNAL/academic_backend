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

from models.department import Department
from repositories.department_repository import DepartmentRepository


# TODO check validations and errors codes
class DepartmentController:

    def __init__(self):
        """
        This is the constructor of the DepartmentController class
        """
        print("Department controller ready")
        self.department_repository = DepartmentRepository()

    def index(self) -> list:
        """

        :return:
        """
        return self.department_repository.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.department_repository.find_by_id(id_)

    def create(self, department_: dict) -> dict:
        """

        :param department_:
        :return:
        """
        print("insert a department")
        department = Department(department_)
        return self.department_repository.save(department)

    def update(self, id_: str, department_: dict) -> dict:
        """

        :param id_:
        :param department_:
        :return:
        """
        department = Department(department_)
        return self.department_repository.update(id_, department)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        return self.department_repository.delete(id_)
