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

from models.student import Student
from repositories.student_repository import StudentRepository


# TODO check validations and errors codes
class StudentController:

    def __init__(self):
        """
        This is the constructor of the StudentController class
        """
        print("Student Controller ready")
        self.student_repository = StudentRepository()

    def index(self) -> list:
        """
        This method returns all students persisted in the db
        :return: student's list
        """
        return self.student_repository.find_all()

    def show(self, id_: str) -> dict:
        """
        This method returns one student based on the database id
        :param id_:
        :return: student
        """
        return self.student_repository.find_by_id(id_)

    def create(self, student_: dict) -> dict:
        """
        This method sends a new student to be persisted into the database
        :param student_: student to save
        :return: student saved with id
        """
        student = Student(student_)
        return self.student_repository.save(student)

    def update(self, id_: str, student_: dict) -> dict:
        """
        This method updates the information of a student
        :param id_: student database id
        :param student_: information to be updated
        :return: student with updates
        """
        student = Student(student_)
        return self.student_repository.update(id_, student)

    def delete(self, id_: str) -> dict:
        """
        Delete a student from the database based in the id
        :param id_: student database id
        :return: confirmation message
        """
        return self.student_repository.delete(id_)
