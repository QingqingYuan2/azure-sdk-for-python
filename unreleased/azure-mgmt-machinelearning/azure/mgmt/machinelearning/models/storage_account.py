# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageAccount(Model):
    """Access information for a storage account.

    :param name: Specifies the name of the storage account.
    :type name: str
    :param key: Specifies the key used to access the storage account.
    :type key: str
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
    }

    def __init__(self, name=None, key=None):
        self.name = name
        self.key = key