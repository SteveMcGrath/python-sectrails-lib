'''
IP Address API Endpoints
========================

.. rst-class:: hide-signature
.. autoclass:: IpAddressesAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from typing import Optional
from .iterators import PageIterator


class IpAddressesAPI(APIEndpoint):
    _path = 'ips'

    def neighbors(self, address: str) -> dict:
        '''
        '''
        return self._get(f'nearby/{address}').json()

    def search(self, query: str, page: Optional[int] = None) -> PageIterator:
        '''
        '''
        return PageIterator(
            self._api,
            _method='POST',
            _payload={'query': query},
            _path='ips/list'
        )

    def stats(self, query: str) -> dict:
        '''
        '''
        return self._post('stats', json={'query': query}).json()

    def whois(self, address: str) -> dict:
        '''
        '''
        return self._get(f'{address}/whois').json()

    def user_agents(self, address: str) -> PageIterator:
        '''
        '''
        return PageIterator(self._api, _path=f'{address}/useragents')
