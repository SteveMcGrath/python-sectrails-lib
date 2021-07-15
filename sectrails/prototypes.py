'''
Prototypes API Endpoints
========================

.. rst-class:: hide-signature
.. autoclass:: PrototypeAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from .iterators import PageIterator


class PrototypeAPI(APIEndpoint):
    _path = 'prototype'

    def dslv2(self, query: str) -> PageIterator:
        '''
        DSLv2 API Endpoint

        Args:
            query (str): DSL Query

        Returns:
            PageIterator: The results iterator

        Example:

            >>> for record in st.prototype.dslv2(query):
            ...     print(record)
        '''
        return PageIterator(
            self._api,
            _method='POST',
            _payload={'query': query},
            _path='prototype/dslv2'
        )
