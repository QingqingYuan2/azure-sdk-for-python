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


class TrackedResource(Model):
    """Describes an Azure tracked resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar location: Location where the resource is stored
    :vartype location: str
    :param kind: Kind of the resource
    :type kind: str
    :param etag: Entity tag is used for comparing two or more entities from
     the same requested resource. ETags may be returned for individual
     resources, and then sent via If-Match / If-None-Match headers for
     concurrency control.
    :type etag: str
    :param tags: A list of key value pairs that describe the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, kind: str=None, etag: str=None, tags=None, **kwargs) -> None:
        super(TrackedResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = None
        self.kind = kind
        self.etag = etag
        self.tags = tags
