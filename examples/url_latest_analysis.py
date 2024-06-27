import sys
from pprint import pprint

from khulnasoft_analyze_sdk import api
from khulnasoft_analyze_sdk.analysis import UrlAnalysis


def get_url_latest_analysis(url: str):
    api.set_global_api('<api-key>')
    analysis = UrlAnalysis.from_latest_analysis(url)
    if analysis:
        pprint(analysis.result())

if __name__ == '__main__':
    get_url_latest_analysis(*sys.argv[1:])