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


class SearchParameters(Model):
    """Parameters specifying the search query and range.

    All required parameters must be populated in order to send to Azure.

    :param top: The number to get from the top.
    :type top: long
    :param highlight: The highlight that looks for all occurences of a string.
    :type highlight: ~azure.mgmt.loganalytics.models.SearchHighlight
    :param query: Required. The query to search.
    :type query: str
    :param start: The start date filter, so the only query results returned
     are after this date.
    :type start: datetime
    :param end: The end date filter, so the only query results returned are
     before this date.
    :type end: datetime
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'top': {'key': 'top', 'type': 'long'},
        'highlight': {'key': 'highlight', 'type': 'SearchHighlight'},
        'query': {'key': 'query', 'type': 'str'},
        'start': {'key': 'start', 'type': 'iso-8601'},
        'end': {'key': 'end', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(SearchParameters, self).__init__(**kwargs)
        self.top = kwargs.get('top', None)
        self.highlight = kwargs.get('highlight', None)
        self.query = kwargs.get('query', None)
        self.start = kwargs.get('start', None)
        self.end = kwargs.get('end', None)
