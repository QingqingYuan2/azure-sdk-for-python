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


class VirtualMachineSshCredentials(Model):
    """Admin credentials for virtual machine.

    :param username: Username of admin account
    :type username: str
    :param password: Password of admin account
    :type password: str
    :param public_key_data: Public key data
    :type public_key_data: str
    :param private_key_data: Private key data
    :type private_key_data: str
    """

    _attribute_map = {
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'public_key_data': {'key': 'publicKeyData', 'type': 'str'},
        'private_key_data': {'key': 'privateKeyData', 'type': 'str'},
    }

    def __init__(self, *, username: str=None, password: str=None, public_key_data: str=None, private_key_data: str=None, **kwargs) -> None:
        super(VirtualMachineSshCredentials, self).__init__(**kwargs)
        self.username = username
        self.password = password
        self.public_key_data = public_key_data
        self.private_key_data = private_key_data