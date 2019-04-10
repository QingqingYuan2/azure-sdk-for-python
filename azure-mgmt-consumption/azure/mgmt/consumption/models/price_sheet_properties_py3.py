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


class PriceSheetProperties(Model):
    """The properties of the price sheet.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar billing_period_id: The id of the billing period resource that the
     usage belongs to.
    :vartype billing_period_id: str
    :ivar meter_id: The meter id (GUID)
    :vartype meter_id: str
    :ivar meter_details: The details about the meter. By default this is not
     populated, unless it's specified in $expand.
    :vartype meter_details: ~azure.mgmt.consumption.models.MeterDetails
    :ivar unit_of_measure: Unit of measure
    :vartype unit_of_measure: str
    :ivar included_quantity: Included quality for an offer
    :vartype included_quantity: decimal.Decimal
    :ivar part_number: Part Number
    :vartype part_number: str
    :ivar unit_price: Unit Price
    :vartype unit_price: decimal.Decimal
    :ivar currency_code: Currency Code
    :vartype currency_code: str
    :ivar offer_id: Offer Id
    :vartype offer_id: str
    """

    _validation = {
        'billing_period_id': {'readonly': True},
        'meter_id': {'readonly': True},
        'meter_details': {'readonly': True},
        'unit_of_measure': {'readonly': True},
        'included_quantity': {'readonly': True},
        'part_number': {'readonly': True},
        'unit_price': {'readonly': True},
        'currency_code': {'readonly': True},
        'offer_id': {'readonly': True},
    }

    _attribute_map = {
        'billing_period_id': {'key': 'billingPeriodId', 'type': 'str'},
        'meter_id': {'key': 'meterId', 'type': 'str'},
        'meter_details': {'key': 'meterDetails', 'type': 'MeterDetails'},
        'unit_of_measure': {'key': 'unitOfMeasure', 'type': 'str'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'decimal'},
        'part_number': {'key': 'partNumber', 'type': 'str'},
        'unit_price': {'key': 'unitPrice', 'type': 'decimal'},
        'currency_code': {'key': 'currencyCode', 'type': 'str'},
        'offer_id': {'key': 'offerId', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(PriceSheetProperties, self).__init__(**kwargs)
        self.billing_period_id = None
        self.meter_id = None
        self.meter_details = None
        self.unit_of_measure = None
        self.included_quantity = None
        self.part_number = None
        self.unit_price = None
        self.currency_code = None
        self.offer_id = None
