'''
Iterators
=========

.. autoclass:: PageIterator
    :members:
'''
from restfly.iterator import APIIterator
from copy import copy


class PageIterator(APIIterator):
    '''
    The API v1 Page Iterator

    Params:
        count (int):
        page (list[dict]):
        page_count (int):
        total (int):
    '''
    page_count = 0
    _path = None
    _params = {}
    _payload = None
    _method = 'GET'


    def _get_page(self):
        params = copy(self._params)
        params['page'] = self.num_pages + 1
        resp = self._api.request(self._method,
                                 self._path,
                                 json=self._payload,
                                 params=params
                                 ).json()
        self.total = resp['record_count']
        self.page = resp['records']
        self.page_count += 1
