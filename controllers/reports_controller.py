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

from repositories.reports_repository import ReportsRepository


class ReportsController:
    def __init__(self):
        """
        This is the constructor of the ReportController class
        """
        self.report_repository = ReportsRepository()

    def report_student_stats(self) -> dict:
        """

        :return:
        """
        return self.report_repository.get_grades_stats()

    # Equivalent to: count votes per tables
    def report_students_enrollments(self, id_: str = "-1") -> list:
        """

        :param id_:
        :return:
        """
        return self.report_repository.get_students_enrollments(id_=id_)

    # Equivalent to: count votes per candidate
    def report_course_enrollments(self, id_: str = "-1") -> list:
        """

        :param id_:
        :return:
        """
        return self.report_repository.get_course_enrollments(id_)

    # Equivalent to: get top n candidates with more votes
    def report_students_more_enrollments(self) -> list:
        """

        :return:
        """
        n = 5
        return self.report_repository.get_students_enrollments(id_="-1", limit=n)

    # Equivalent to: count votes per political party
    def report_department_enrollments(self) -> list:
        """

        :return:
        """
        return self.report_repository.get_department_enrollments()

    # Equivalent to: percentual distribution of political party winners
    def report_department_distribution(self) -> list:
        """

        :return:
        """
        return self.report_repository.get_departments_distribution()
