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

from .cluster_event import ClusterEvent


class ClusterNewHealthReportEvent(ClusterEvent):
    """Cluster Health Report Created event.

    All required parameters must be populated in order to send to Azure.

    :param event_instance_id: Required. The identifier for the FabricEvent
     instance.
    :type event_instance_id: str
    :param category: The category of event.
    :type category: str
    :param time_stamp: Required. The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Required. Constant filled by server.
    :type kind: str
    :param source_id: Required. Id of report source.
    :type source_id: str
    :param property: Required. Describes the property.
    :type property: str
    :param health_state: Required. Describes the property health state.
    :type health_state: str
    :param time_to_live_ms: Required. Time to live in milli-seconds.
    :type time_to_live_ms: long
    :param sequence_number: Required. Sequence number of report.
    :type sequence_number: long
    :param description: Required. Description of report.
    :type description: str
    :param remove_when_expired: Required. Indicates the removal when it
     expires.
    :type remove_when_expired: bool
    :param source_utc_timestamp: Required. Source time.
    :type source_utc_timestamp: datetime
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'source_id': {'required': True},
        'property': {'required': True},
        'health_state': {'required': True},
        'time_to_live_ms': {'required': True},
        'sequence_number': {'required': True},
        'description': {'required': True},
        'remove_when_expired': {'required': True},
        'source_utc_timestamp': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'category': {'key': 'Category', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'source_id': {'key': 'SourceId', 'type': 'str'},
        'property': {'key': 'Property', 'type': 'str'},
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'time_to_live_ms': {'key': 'TimeToLiveMs', 'type': 'long'},
        'sequence_number': {'key': 'SequenceNumber', 'type': 'long'},
        'description': {'key': 'Description', 'type': 'str'},
        'remove_when_expired': {'key': 'RemoveWhenExpired', 'type': 'bool'},
        'source_utc_timestamp': {'key': 'SourceUtcTimestamp', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(ClusterNewHealthReportEvent, self).__init__(**kwargs)
        self.source_id = kwargs.get('source_id', None)
        self.property = kwargs.get('property', None)
        self.health_state = kwargs.get('health_state', None)
        self.time_to_live_ms = kwargs.get('time_to_live_ms', None)
        self.sequence_number = kwargs.get('sequence_number', None)
        self.description = kwargs.get('description', None)
        self.remove_when_expired = kwargs.get('remove_when_expired', None)
        self.source_utc_timestamp = kwargs.get('source_utc_timestamp', None)
        self.kind = 'ClusterNewHealthReport'
