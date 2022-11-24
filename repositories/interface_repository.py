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

import certifi
import json
import pymongo
from typing import Generic, TypeVar, get_args
from bson import ObjectId, DBRef

T = TypeVar('T')


class InterfaceRepository(Generic[T]):

    def __init__(self):
        """
        This is the constructor of the InterfaceRepository class.
        Here is where we make the generalization, so based on the
        class T, both collection and connection are defined.
        """
        ca = certifi.where()
        data_config = self.load_file_config()
        client = pymongo.MongoClient(data_config.get("db-connection"), tlsCAFile=ca)
        self.data_base = client[data_config.get("db-name")]
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()
        self.current_collection = self.data_base[self.collection]

    @staticmethod
    def load_file_config() -> dict:
        """

        :return:
        """
        with open("config.json") as file:
            data = json.load(file)
        return data

    def process_collection_list(self, list_):
        dataset = []
        for document in list_:
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_all(self) -> list:
        """

        :return:
        """
        return self.process_collection_list(self.current_collection.find())

    def find_by_id(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        document = self.current_collection.find_one({'_id': ObjectId(id_)})
        document = self.get_values_db_ref(document)
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            document = {}
        return document

    def save(self, item: T) -> dict:
        """

        :param item:
        :return:
        """
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            id_ = item._id
            delattr(item, '_id')
            self.update(id_, item)
        else:
            _id = self.current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    def update(self, id_: str, item: T) -> dict:
        """

        :param id_:
        :param item:
        :return:
        """
        _id = ObjectId(id_)
        item = item.__dict__
        update_item = {"$set": item}
        self.current_collection.update_one({'_id': _id}, update_item)
        return self.find_by_id(id_)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        _id = ObjectId(id_)
        result = self.current_collection.delete_one({'_id': _id})
        return {"deleted_count": result.deleted_count}

    def query(self, query: dict) -> list:
        """

        :param query:
        :return:
        """
        return self.process_collection_list(self.current_collection.find(query))

    def query_aggregation(self, query: list) -> list:
        """

        :param query:
        :return:
        """
        return self.process_collection_list(self.current_collection.aggregate(query))

    def get_values_db_ref(self, document: dict) -> dict:
        """

        :param document:
        :return:
        """
        keys = document.keys()
        for key in keys:
            if isinstance(document.get(key), DBRef):
                collection_ = self.data_base[document[key].collection]
                value = collection_.find_one({'_id': ObjectId(document[key].id)})
                value['_id'] = value['_id'].__str__()
                document[key] = self.get_values_db_ref(value)
            elif isinstance(document.get(key), list) and len(document.get(key)) > 0:
                document[key] = self.get_values_db_ref_from_list(document[key])
            elif isinstance(document.get(key), dict):
                document[key] = self.get_values_db_ref(document.get(key))
        return document

    def get_values_db_ref_from_list(self, list_: list) -> list:
        """

        :param list_:
        :return:
        """
        processed_list = []
        collection_ = self.data_base[list_[0]._id.collection]
        for item in list_:
            _id = ObjectId(item._id)
            sub_document = collection_.find_one({'_id': _id})
            sub_document['_id'] = sub_document['_id'].__str__()
            processed_list.append(sub_document)
        return processed_list

    def transform_object_ids(self, document: dict) -> dict:
        """

        :param document:
        :return:
        """
        for key in document.keys():
            if isinstance(document.get(key), ObjectId):
                document[key] = document[key].__str__()
            elif isinstance(document.get(key), list):
                document[key] = self.format_list(document.get(key))
            elif isinstance(document[key], dict):
                document[key] = self.transform_object_ids(document.get(key))
        return document

    @staticmethod
    def format_list(list_: list) -> list:
        """

        :param list_:
        :return:
        """
        processed_list = []
        for item in list_:
            if isinstance(item, ObjectId):
                temp = item.__str__()
                processed_list.append(temp)
        if len(processed_list) == 0:
            processed_list = list_
        return processed_list

    def transform_refs(self, item: T) -> T:
        """

        :param item:
        :return:
        """
        item_dict = item.__dict__
        for key in item_dict.keys():
            if item_dict.get(key).__str__().count("object") == 1:
                object_ = self.object_to_db_ref(getattr(item, key))
                setattr(item, key, object_)
        return item

    @staticmethod
    def object_to_db_ref(item: T) -> DBRef:
        """

        :param item:
        :return:
        """
        collection_ = item.__class__.__name__.lower()
        return DBRef(collection_, ObjectId(item._id))
