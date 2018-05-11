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


class StreamingLocatorUserDefinedContentKey(Model):
    """Describes the properties of a user-defined content key in the Streaming
    Locator.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. ID of Content Key
    :type id: str
    :param label: The Content Key description
    :type label: str
    :param value: The Content Key secret
    :type value: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StreamingLocatorUserDefinedContentKey, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.label = kwargs.get('label', None)
        self.value = kwargs.get('value', None)