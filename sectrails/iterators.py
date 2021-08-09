'''
Iterators
=========

.. autoclass:: PageIterator
    :members:
'''
import warnings
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

        # if we are about to request any pages over 100, then we need to
        # terminate the iterator.
        if params['page'] > 100:
            warnings.warn('Total results exceeded 100 pages.')
            raise StopIteration()

        # make the API call
        resp = self._api._req(self._method,
                              self._path,
                              json=self._payload,
                              params=params
                              ).json()

        # update the record counts, page counts, and load the next page of
        # content into the page list.
        self.total = resp['record_count']
        self.page = resp['records']
        self.page_count += 1
        if self.total > 100000:
            warnings.warn(('The API limits the results to the first 100,000 '
                           'of the {self.total} records available.'))
