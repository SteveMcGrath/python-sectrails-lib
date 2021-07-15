'''
Feeds API Endpoints
===================

.. rst-class:: hide-signature
.. autoclass:: FeedsAPI
    :members:
'''
from restfly.endpoint import APIEndpoint
from typing import Optional, Literal, Union
from arrow import Arrow
from io import BytesIO, BufferedWriter
import arrow
import datetime


class FeedsAPI(APIEndpoint):
    _path = 'feeds'

    def domains(self,
                record_type: Literal['all', 'deleted', 'new', 'registered'],
                fobj: Optional[Union[BytesIO, BufferedWriter]] = None,
                filter: Optional[Literal['cctld', 'gtld']] = None,
                tld: Optional[str] = None,
                ns: bool = False,
                date: Optional[Union[str, int, Arrow, datetime.date]] = None
                ) -> dict:
        if date:
            date = arrow.get(date).format('YYYY-MM-DD')
        resp = self._get(f'domains/{record_type}', params={
            'filter': filter,
            'tld': tld,
            'ns': str(ns).lower(),
            'date': date
        })

        if not fobj:
            fobj = BytesIO()

        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                fobj.write(chunk)

        return fobj

    def dmarc(self,
              record_type: Literal['all', 'new'],
              fobj: Optional[Union[BytesIO, BufferedWriter]] = None,
              date: Optional[Union[str, int, Arrow, datetime.date]] = None
              ) -> dict:
        resp = self._get('dmarc/{record_type}',
                         params={'date': arrow.get(date).format('YYYY-MM-DD')})

        if not fobj:
            fobj = BytesIO()

        for chunk in resp.iter_content(chunk_size=1024):
            if chunk:
                fobj.write(chunk)

        return fobj

    def subdomains(self,
                   record_type: Literal['all', 'new', 'deleted'],
                   filter: Optional[Literal['bytld']] = None,
                   tld: Optional[str] = None,
                   date: Optional[Union[str, int, Arrow, datetime.date]] = None
                   ) -> dict:
        if date:
            date = arrow.get(date).format('YYYY-MM-DD')
        return self._get(f'subdomains/{record_type}', params={
            'filter': filter,
            'tld': tld,
            'date': date
        })
