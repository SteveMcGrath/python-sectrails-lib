'''
Domain API Endpoints
====================

.. rst-class:: hide-signature
.. autoclass:: DomainAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from restfly.utils import dict_clean
from typing import Optional, Literal
from .iterators import PageIterator


class DomainAPI(APIEndpoint):
    _path = 'domain'

    def details(self, domain: str) -> dict:
        '''
        Returns the current data about the given hostname.

        :st-api:`API Documentation <domain-details>`

        Example:
            >>> st.domain.details('google.com')
            {
                "hostname": "google.com",
                "endpoint": "/v1/domain/example.net",
                "current_dns": {
                    "a": {},
                    "aaaa": {},
                    "mx": {},
                    "ns": {},
                    "soa": {},
                    "txt": {}
                },
                "alexa_rank":123
            }
        '''
        return self._get(domain).json()

    def subdomains(self,
                   domain: str,
                   children_only: bool = False,
                   include_inactive: bool = True
                   ) -> dict:
        '''
        Returns the child and sibling subdomains for a given hostname.

        :st-api:`API Documentation <domain-subdomains>`

        Args:
            domain (str): The hostname to query with.
            children_only (optional, bool): Only return child subdomains.
            include_inactive (optional, bool):
                Include domains that dont have active records.

        Example:
            >>> st.domain.subdomains('google.com')
            ["www", "mail", "vpn"]
        '''
        return self._get(f'{domain}/subdomains', params={
            'children_only': str(children_only).lower(),
            'include_inactive': str(include_inactive).lower()
        }).json()['subdomains']

    def tags(self, domain: str) -> dict:
        '''
        '''
        return self._get(f'{domain}/tags').json()

    def whois(self, domain: str) -> dict:
        '''
        '''
        return self._get(f'{domain}/whois').json()

    def associated(self,
                   domain: str,
                   page: Optional[int] = None
                   ) -> PageIterator:
        '''
        '''
        return PageIterator(self._api, _path=f'domain/{domain}/associated')

    def ssl_certificates(self,
                         domain: str,
                         include_subdomains: bool = False,
                         status: Literal['valid', 'all', 'expired'] = 'valid',
                         page: Optional[int] = None
                         ) -> PageIterator:
        '''
        '''
        return PageIterator(
            self._api,
            _path=f'domain/{domain}/ssl',
            _params={
                'include_subdomains': str(include_subdomains).lower(),
                'status': status,
            }
        )
        #return self._get(f'{domain}/ssl', params={
        #    'include_subdomains': str(include_subdomains).lower(),
        #    'status': status,
        #    'page': page
        #}).json()

    def search(self,
               query: Optional[str] = None,
               filter: Optional[dict] = None,
               include_ips: bool = False,
               scroll: bool = False,
               ) -> dict:
        '''
        '''

        return self._api.post('domains/list', params={
            'include_ips': include_ips,
            'page': page,
            'scroll': scroll
        }, json=dict_clean({
            'query': query,
            'filter': filter
        })).json()

    def stats(self,
              query: Optional[str] = None,
              filter: Optional[dict] = None,
              ) -> dict:
        return self._api.post('domains/stats', json=dict_clean({
            'query': query,
            'filter': filter
        })).json()
