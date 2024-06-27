import datetime
from typing import List
from typing import Optional

from khulnasoft_analyze_sdk import consts
from khulnasoft_analyze_sdk._account_api import AccountApi
from khulnasoft_analyze_sdk.api import KhulnasoftApiClient


class Account:
    def __init__(self, account_id: str, account_details: dict, *, api: KhulnasoftApiClient):
        self._api = AccountApi(api)
        self.account_id: str = account_id
        self.details = account_details

    def __eq__(self, other):
        return self is other or isinstance(other, Account) and self.account_id == other.account_id

    @property
    def name(self) -> str:
        return self.details['account_name']

    @property
    def email(self) -> Optional[str]:
        return self.details['account_email'] if 'account_email' else None

    @property
    def created_time(self) -> Optional[datetime.datetime]:
        if 'created_time' in self.details:
            return datetime.datetime.strptime(self.details['created_time'], consts.DEFAULT_DATE_FORMAT)
        return None

    @property
    def last_sign_in_time(self) -> Optional[datetime.datetime]:
        if 'last_sign_in_time' in self.details:
            return datetime.datetime.strptime(self.details['last_sign_in_time'], consts.DEFAULT_DATE_FORMAT)
        return None

    @classmethod
    def from_account_id(cls, account_id: str, api: KhulnasoftApiClient = None) -> Optional['Account']:
        """
        Get details about an account.

        :param account_id: The account id
        :param api: The API connection to Khulnasoft.
        :return: The account
        """
        account_details = AccountApi(api).get_account(account_id)
        if account_details:
            return cls(account_id, account_details, api=api)
        return None

    @classmethod
    def from_myself(cls, api: KhulnasoftApiClient = None) -> 'Account':
        """
        Get information about the current account

        :param api: The API connection to Khulnasoft.
        :return: The account
        """
        account_details = AccountApi(api).get_my_account()
        return cls(account_details['account_id'], account_details, api=api)

    @classmethod
    def get_organization_account(cls, api: KhulnasoftApiClient = None) -> List['Account']:
        """
        Get all accounts in the organization.

        :param api: The API connection to Khulnasoft.
        :return: A list of accounts associated with the organization
        """
        return [cls(account_details['account_id'], account_details, api=api) for account_details in AccountApi(api).get_organization_accounts()]

    @classmethod
    def get_my_quota(cls, api: KhulnasoftApiClient = None, raise_on_no_file_quota=False, raise_on_no_endpoint_quota=False) -> dict:
        """
        Get quota usage of the current account

        :param api: The API connection to Khulnasoft.
        :param raise_on_no_file_quota: should raise :data:`khulnasoft_analyze_sdk.errors.InsufficientQuotaError` if no file quota left
        :param raise_on_no_endpoint_quota: should raise :data:`khulnasoft_analyze_sdk.errors.InsufficientQuotaError` if no endpoint quota left
        :return:
        """
        return AccountApi(api).get_my_quota(raise_on_no_file_quota, raise_on_no_endpoint_quota)
