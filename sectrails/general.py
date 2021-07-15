'''
General API Endpoints
=====================

.. rst-class:: hide-signature
.. autoclass:: GeneralAPI
    :members:
'''
from restfly.endpoint import APIEndpoint


class GeneralAPI(APIEndpoint):
    def ping(self) -> bool:
        '''
        Endpoint to test authentication to the API.

        :st-api:`API Documentation <ping>`

        Returns:
            bool: True if authenticated, False otherwise.

        Example:

            >>> if st.general.ping():
            ...     print('Authentication Successful!')
        '''
        return self._api.get('ping').json()['success']

    def usage(self) -> dict:
        '''
        Usage statistics for the current month.

        :st-api:`API Documentation <usage>`

        Returns:
            dict: Usage statistics dictionary

        Example:

            >>> st.general.usage()
            {"current_monthly_usage": 100, "allowed_monthly_usage": 10000}
        '''
        return self._api.get('account/usage').json()
