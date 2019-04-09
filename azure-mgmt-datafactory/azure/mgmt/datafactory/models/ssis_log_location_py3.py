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


class SSISLogLocation(Model):
    """SSIS package exection log location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param log_path: Required. The SSIS package execution log path. Type:
     string (or Expression with resultType string).
    :type log_path: object
    :ivar type: Required. The type of SSIS log location. Default value: "File"
     .
    :vartype type: str
    :param access_credential: The package execution log access credential.
    :type access_credential:
     ~azure.mgmt.datafactory.models.SSISAccessCredential
    """

    _validation = {
        'log_path': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'log_path': {'key': 'logPath', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'access_credential': {'key': 'typeProperties.accessCredential', 'type': 'SSISAccessCredential'},
    }

    type = "File"

    def __init__(self, *, log_path, access_credential=None, **kwargs) -> None:
        super(SSISLogLocation, self).__init__(**kwargs)
        self.log_path = log_path
        self.access_credential = access_credential
