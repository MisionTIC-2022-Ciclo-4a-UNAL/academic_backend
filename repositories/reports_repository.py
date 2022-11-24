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

from bson import ObjectId

from models.enrollment import Enrollment
from repositories.interface_repository import InterfaceRepository


class ReportsRepository(InterfaceRepository[Enrollment]):

    def get_grades_stats(self):
        query_aggregation = {
            "$group": {
                "_id": "$student",
                "count": {"$sum": 1}
            }
        }
        query_sort = {
            "$sort": {
                "count": 1
            }
        }
        query_limit = {
            "$limit": 15
        }
        pipeline = [query_aggregation, query_sort, query_limit]
        return self.query_aggregation(pipeline)

    def get_students_enrollments(self, id_: str = "-1", limit: int = None) -> list:
        """

        :param limit:
        :param id_:
        :return:
        """
        # Equivalent to WHERE student_fk = ObjectId(id_)
        query_match = {}
        if id != "-1":
            query_match = {
                "$match": {
                    "student.$id": ObjectId(id_)
                }
            }
        # Equivalent to make a INNER JOIN
        query_lookup = {
            "$lookup": {
                "from": "student",
                "localField": "student.$id",
                "foreignField": "_id",
                "as": "students_info"
            },
            "$unwind": "$students_info"
        }
        # Equivalent to GROUP BY
        query_group = {
            "$group": {
                "_id": "$students_info",
                "enrollments": {"$sum": 1}
            }
        }
        # Clean the response, using equivalent to ALIAS and ORDER BY
        query_add_fields = {
            "$addFields": {
                "name": "$_id.name",
                "lastname": "$_id.lastname",
                "personal_id": "$_id.personal_id",
                "_id": "$_id._id"
            },
            "$sort": {
                "enrollments": 1
            }
        }
        query_limit = {}
        if limit:
            query_limit = {
                "$limit": limit
            }
        pipeline = [query_match, query_lookup, query_group, query_add_fields, query_limit]
        return self.query_aggregation(pipeline)

    def get_course_enrollments(self, id_: str) -> list:
        """

        :param id_:
        :return:
        """
        # Equivalent to WHERE course_fk = ObjectId(id_)
        query_match = {}
        if id != "-1":
            query_match = {
                "$match": {
                    "course.$id": ObjectId(id_)
                }
            }
        # Equivalent to make a INNER JOIN
        query_lookup = {
            "$lookup": {
                "from": "course",
                "localField": "course.$id",
                "foreignField": "_id",
                "as": "course_info"
            },
            "$unwind": "$course_info"
        }
        # Equivalent to GROUP BY
        query_group = {
            "$group": {
                "_id": "$course_info",
                "enrollments": {"$sum": 1}
            }
        }
        # Clean the response, using equivalent to ALIAS and ORDER BY DESC
        query_add_fields = {
            "$addFields": {
                "name": "$_id.name",
                "credits": "$_id.credits",
                "_id": "$_id._id"
            },
            "$sort": {
                "enrollments": -1
            }
        }
        pipeline = [query_match, query_lookup, query_group, query_add_fields]
        return self.query_aggregation(pipeline)

    def get_department_enrollments(self) -> list:
        """

        :return:
        """
        # Equivalent to make an INNER JOIN courses
        query_preprocess_courses = {
            "$lookup": {
                "from": "course",
                "localField": "course.$id",
                "foreignField": "_id",
                "as": "course_info"
            },
            "$unwind": "$course_info"
        }
        # Equivalent to make a GROUP BY courses
        query_group_courses = {
            "$group": {
                "_id": "$course_info",
                "count": {"$sum": 1}
            },
            "$addFields": {
                "department": "$_id.department"
            }
        }
        # Equivalent to make an INNER JOIN departments
        query_process_departments = {
            "$lookup": {
                "from": "department",
                "localField": "department.$id",
                "foreignField": "_id",
                "as": "department_info"
            },
            "$unwind": "$department_info"
        }
        # Equivalent to make GROUP BY and ORDER BY departments
        query_group_departments = {
            "$group": {
                "_id": "$department_info",
                "enrollments": {"$sum": "$count"}
            },
            "$addFields": {
                "name": "$_id.name",
                "_id": "$_id._id"
            }
        }
        pipeline = [query_preprocess_courses, query_group_courses, query_process_departments, query_group_departments]
        return self.query_aggregation(pipeline)

    def get_departments_distribution(self) -> list:
        """

        :return:
        """
        winners = 15
        # Equivalent to make an INNER JOIN courses
        query_preprocess_courses = {
            "$lookup": {
                "from": "course",
                "localField": "course.$id",
                "foreignField": "_id",
                "as": "course_info"
            },
            "$unwind": "$course_info"
        }
        # Equivalent to make a GROUP BY courses
        query_group_courses = {
            "$group": {
                "_id": "$course_info",
                "count": {"$sum": 1}
            },
            "$sort": {
                "enrollments": -1
            },
            "$limit": winners,
            "$addFields": {
                "department": "$_id.department"
            }
        }
        # Equivalent to make an INNER JOIN departments
        query_process_departments = {
            "$lookup": {
                "from": "department",
                "localField": "department.$id",
                "foreignField": "_id",
                "as": "department_info"
            },
            "$unwind": "$department_info"
        }
        # Equivalent to make GROUP BY and ORDER BY departments
        query_group_departments = {
            "$group": {
                "_id": "$department_info",
                "enrollments": {"$sum": "$count"}
            },
            "$addFields": {
                "name": "$_id.name",
                "_id": "$_id._id"
            }
        }
        pipeline = [query_preprocess_courses, query_group_courses, query_process_departments, query_group_departments]
        return self.query_aggregation(pipeline)
