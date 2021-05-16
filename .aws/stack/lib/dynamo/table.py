from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    UnicodeSetAttribute,
    NumberAttribute,
    BooleanAttribute,
    MapAttribute,
    UTCDateTimeAttribute
)
from datetime import datetime


class WatchingList(Model):
    """
    References:
        https://pynamodb.readthedocs.io/en/latest/index.html

    Notes:
        Be aware that the models defined here should be consistent with
        dynamo stack in cdk.
    """
    class Meta:
        table_name = 'watching-list'
        region = 'us-east-1'

    ticker_symbol = UnicodeAttribute(hash_key=True)
