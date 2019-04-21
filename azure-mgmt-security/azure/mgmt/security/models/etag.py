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


class ETag(Model):
    """Entity tag is used for comparing two or more entities from the same
    requested resource. ETags may be returned for individual resources, and
    then sent via If-Match / If-None-Match headers for concurrency control. .

    :param etag: Entity tag is used for comparing two or more entities from
     the same requested resource. ETags may be returned for individual
     resources, and then sent via If-Match / If-None-Match headers for
     concurrency control.
    :type etag: str
    """

    _attribute_map = {
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ETag, self).__init__(**kwargs)
        self.etag = kwargs.get('etag', None)
