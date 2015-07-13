from iris_sdk.client import Client
from iris_sdk.include.xml_consts import *
from iris_sdk.models.account import Account

class GetDisconnectedNumbers():

    def __init__(self, filename=None):

        self._client = Client(filename=filename)

        acc = Account(client=self._client)

        print("\n--- Disconnected numbers ---\n")

        disc_numbers = \
            acc.disconnected_numbers.list(
                {XML_PARAM_PAGE: 1, XML_PARAM_SIZE: 20})

        print("total for search: " + \
            (acc.disconnected_numbers.total_count or "0"))

        for phone_number in disc_numbers.items:
            print(phone_number)

        print("total: " + acc.disconnected_numbers.totals.get().count)