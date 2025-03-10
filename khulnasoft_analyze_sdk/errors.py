from typing import Optional

import requests


def _parse_erroneous_response(response: requests.Response):
    try:
        data = response.json()
        return data.get('error', '')
    except ValueError:
        return ''


class KhulnasoftError(Exception):
    pass


class UnsupportedOnPremiseVersionError(KhulnasoftError):
    pass


UnsupportedOnPremiseVersion = UnsupportedOnPremiseVersionError


class ServerError(KhulnasoftError):
    def __init__(self, message: str, response: requests.Response):
        self.response = response
        detailed_error = _parse_erroneous_response(response)
        if detailed_error:
            message = f'{message}. Error:{detailed_error}'
        super().__init__(message)


class AnalysisHasAlreadyBeenSentError(KhulnasoftError):
    def __init__(self):
        super().__init__('Analysis already been sent')


AnalysisHasAlreadyBeenSent = AnalysisHasAlreadyBeenSentError


class IndexHasAlreadyBeenSentError(KhulnasoftError):
    def __init__(self):
        super().__init__('Index already been sent')


IndexHasAlreadyBeenSent = IndexHasAlreadyBeenSentError


class FamilyNotFoundError(KhulnasoftError):
    def __init__(self, family_id: str):
        super().__init__(f'Family not found: {family_id}')


class HashDoesNotExistError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Hash was not found', response)


class FileTooLargeError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('File is too large', response)


class ReportDoesNotExistError(KhulnasoftError):
    def __init__(self):
        super().__init__('Report was not found')


class AnalysisIsAlreadyRunningError(ServerError):
    def __init__(self, response: requests.Response, running_analysis_id: Optional[str]):
        super().__init__('Analysis already running', response)
        self.analysis_id = running_analysis_id


AnalysisIsAlreadyRunning = AnalysisIsAlreadyRunningError


class InsufficientQuotaError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Insufficient quota', response)


InsufficientQuota = InsufficientQuotaError


class GlobalApiIsNotInitializedError(KhulnasoftError):
    def __init__(self):
        super().__init__('Global API is not initialized')


GlobalApiIsNotInitialized = GlobalApiIsNotInitializedError


class AnalysisIsStillRunningError(KhulnasoftError):
    def __init__(self):
        super().__init__('Analysis is still running')


AnalysisIsStillRunning = AnalysisIsStillRunningError


class AnalysisFailedError(KhulnasoftError):
    def __init__(self):
        super().__init__('Analysis failed')


class InvalidApiKeyError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Invalid api key', response)


InvalidApiKey = InvalidApiKeyError


class IndexFailedError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Index operation failed', response)


IndexFailed = IndexFailedError


class OperationStillRunningError(KhulnasoftError):
    def __init__(self, operation):
        super().__init__(f'{operation} is still running')


SubAnalysisOperationStillRunning = OperationStillRunningError
SubAnalysisOperationStillRunningError = OperationStillRunningError


class SubAnalysisNotFoundError(KhulnasoftError):
    def __init__(self, analysis_id: str):
        super().__init__(f'analysis {analysis_id} is not found')


class InsufficientPermissionsError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Account does not have permission to this route', response)


class AlertError(KhulnasoftError):
    pass


class InvalidAlertMappingError(AlertError):
    def __init__(self, response: requests.Response):
        super().__init__('Bad request - the mapping is probably malformed', response)


class AlertInProgressError(AlertError):
    def __init__(self, alert_id: str):
        super().__init__(f'The alert {alert_id} is being processed at the moment, please try again later')


class AlertNotFoundError(AlertError):
    def __init__(self, alert_id: str):
        super().__init__(f'The given alert does not exist - {alert_id}')


class InvalidAlertArgumentError(AlertError):
    def __init__(self, message: str):
        super().__init__(message)


class UrlOfflineError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Url is offline', response)


class InvalidUrlError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Invalid url', response)


class AnalysisSkippedByRuleError(ServerError):
    def __init__(self, response: requests.Response):
        super().__init__('Analysis skipped by rule', response)
