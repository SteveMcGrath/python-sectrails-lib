'''
History API Endpoints
=====================

.. rst-class:: hide-signature
.. autoclass:: HistoryAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from typing import Optional, Literal


class HistoryAPI(APIEndpoint):
    _path = 'history'

    def dns(self,
            domain: str,
            record_type: Literal['a', 'aaaa', 'mx', 'ns', 'soa', 'txt'],
            page: Optional[int]
            ) -> dict:
        return self._get(f'{domain}/dns/{record_type}',
                         params={'page': page}).json()

    def whois(self, domain: str, page: Optional[int]):
        return self._get(f'{domain}/whois', params={'page': page}).json()
