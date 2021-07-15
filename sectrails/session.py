'''
SecurityTrails Connection Class
===============================

.. autoclass:: SecurityTrails
    :members:
'''
from restfly.session import APISession
from typing import Optional
from .version import version
from .company import CompanyAPI
from .domain import DomainAPI
from .history import HistoryAPI
from .general import GeneralAPI
from .ipaddress import IpAddressesAPI
from .feeds import FeedsAPI
from .prototypes import PrototypeAPI
import os


class SecurityTrails(APISession):
    '''
    This is the base connection class to be used for communication with the
    SecurityTrails API.  All of the different API endpoint modules are then
    attached to this base class.
    '''
    _url = 'https://api.securitytrails.com/v1'
    _lib_name = 'pySecurityTrails'
    _lib_version = version

    def _authenticate(self, api_key: Optional[str] = None, **kwargs) -> None:
        if not api_key and os.getenv('SECURITY_TRAILS_API_KEY'):
            api_key = os.getenv('SECURITY_TRAILS_API_KEY')
        self._session.headers.update({
            'APIKEY': api_key
        })

    @property
    def company(self) -> CompanyAPI:
        '''
        The interface object for the :doc:`Company API Endpoints <company>`.
        '''
        return CompanyAPI(self)

    @property
    def domain(self) -> DomainAPI:
        '''
        The interface object for the :doc:`Domain API Endpoints <domain>`.
        '''
        return DomainAPI(self)

    @property
    def feed(self) -> FeedsAPI:
        '''
        The interface object for the :doc:`Feed API Endpoints <feeds>`.
        '''
        return FeedsAPI(self)

    @property
    def general(self) -> GeneralAPI:
        '''
        The interface object for the :doc:`General API Endpoints <general>`.
        '''
        return GeneralAPI(self)

    @property
    def history(self) -> HistoryAPI:
        '''
        The interface object for the :doc:`History API Endpoints <history>`.
        '''
        return HistoryAPI(self)

    @property
    def ip(self) -> IpAddressesAPI:
        '''
        The interface object for the
        :doc:`IP Address API Endpoints <ipaddress>`.
        '''
        return IpAddressesAPI(self)

    @property
    def prototype(self) -> PrototypeAPI:
        '''
        The interface object for the
        :doc:`Prototype API Endpoints <prototypes>`.
        '''
        return PrototypeAPI(self)
