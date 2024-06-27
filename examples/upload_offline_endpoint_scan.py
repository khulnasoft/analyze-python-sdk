import sys
from pprint import pprint

from khulnasoft_sdk import api
from khulnasoft_sdk.endpoint_analysis import EndpointAnalysis


def send_file_with_wait(offline_scan_directory: str):
    api.set_global_api('api-key')
    analysis = EndpointAnalysis(offline_scan_directory=offline_scan_directory)
    analysis.send(wait=True)
    pprint(analysis.result())

if __name__ == '__main__':
    send_file_with_wait(*sys.argv[1:])
