'''
Company API Endpoints
=====================

.. rst-class:: hide-signature
.. autoclass:: CompanyAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from typing import List


class CompanyAPI(APIEndpoint):
    _path = 'company'

    def details(self, domain: str) -> dict:
        '''
        Returns details for the company domain

        :st-api:`API Documentation <company-details>`

        Args:
            domain (str): Domain to retrieve

        Returns:
            dict: The response object

        Example:

            >>> st.company.details('google.com')
            {"domain": "google.com", "name": "Google LLC"}
        '''
        return self._get(domain).json()['record']

    def associated_ips(self, domain: str) -> List[dict]:
        '''
        Returns the associated IPs for a company domain.  Data is based on
        whois data with the names matched to the domains.

        :st-api:`API Documentation <company-associated-ips>`

        Args:
            domain (str): Domain to retrieve

        Returns:
            list: List of records.

        Example:

            >>> st.company.associated_ips('google.com')
            [{"cidr": "1.0.0.0/24"}]
        '''
        return self._get(f'{domain}/associated-ips').json()['records']
