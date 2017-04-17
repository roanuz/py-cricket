#!/usr/bin/env python
#
# Copyright 2016  Roanuz Softwares Private Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import uuid
import json


class RcaFileStorageHandler():
    """
    The RcaFileStorageHandler create a text file and save required access
        details as a form of string of dictinary.

        The file will contains following
        access_token : string
        expires : timestamp
        device_id : string

        Example:

        '{ "access_token": "xxxxxxxxxxxxxxxxxxxxxxxxx",
            "expires": "1456571889.0",
            "device_id": "9e6f5ec8-dc7a-11e5-aab3-4cbb5882d7c3"
        }'

    """

    def __init__(self, path=None, name='token.txt'):
        """
            Initialize the file path and name.

        Arg:
        path (optinal) : You have to pass the file path otherwise file
                            will create on current running path
        name (optinal) : File name to your file, defult it will the
        name "token.txt".
        """
        if path and name:
            self.file = path + name
        else:
            self.file = name

    def set_value(self, key, value):
        """
        Set key value to the file.

        The fuction will be make the key and value to dictinary formate.
        If its exist then it will update the current new key value to
        the file.
        Arg:
        key : cache key
        value : cache value
        """
        file_cache = self.read_file()
        if file_cache:
            file_cache[key] = value
        else:
            file_cache = {}
        file_cache[key] = value
        self.update_file(file_cache)

    def get_value(self, key):
        """
        Return the file key value from file.
        Arg:
            key : cache key
        Return:
            value of the key
        """
        file_cache = self.read_file()
        return file_cache[key]

    def has_value(self, key):
        """Checking the available of key and return True if it's exist
        otherwise will be False.


        Arg:
        key : cache key
        Return:
        Boolean True/False


        """
        file_cache = self.read_file()
        return key in file_cache

    def delete_value(self, key):
        """
        Delete the key if the token is expired.

        Arg:
        key : cache key
        """
        response = {}
        response['status'] = False
        response['msg'] = "key does not exist"

        file_cache = self.read_file()
        if key in file_cache:
            del file_cache[key]
            self.update_file(file_cache)
            response['status'] = True
            response['msg'] = "success"
        return response

    # TODO : If key does not exist

    def new_device_id(self):
        """
        Creating a new device_id for user.
        """
        return str(uuid.uuid1())  # create unique device id.

    def read_file(self):
        """
        Open the file and assiging the permission to read/write and
        return the content in json formate.

        Return : json data
        """
        file_obj = open(self.file, 'a+')
        content = file_obj.read()
        file_obj.close()
        if content:
            content = json.loads(content)
            return content
        else:
            return False

    def update_file(self, content):
        """
        It will convert json content to json string and update into file.

        Return:
        Boolean True/False
        """
        updated_content = json.dumps(content)
        file_obj = open(self.file, 'w')
        file_obj.write(str(updated_content))
        file_obj.close()
        return True


class RcaStorageHandler():
    """
    RcaStorageHandler class is used to store temperary token.

        The RcaStorageHandler object will be temperarly store the
        token value and user can use the token value to access the other
        functions
    """

    def __init__(self):
        self.ca_cache = {}

    def set_value(self, key, value):
        self.ca_cache[key] = value

    def get_value(self, key):
        return self.ca_cache[key]

    def has_value(self, key):
        return key in self.ca_cache

    def delete_value(self, key):
        response = {}
        response['status'] = False
        response['msg'] = "key does not exist"

        if key in self.ca_cache:
            del self.ca_cache[key]
            response['status'] = True
            response['msg'] = "success"

    def new_device_id(self):
        return str(uuid.uuid1())  # create unique device id.
