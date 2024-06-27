import sys

from khulnasoft_sdk import api
from khulnasoft_sdk import family as khulnasoft_family


def search_family(family_name: str):
    api.set_global_api('<api_key>')
    family = khulnasoft_family.get_family_by_name(family_name)
    print(family.name)
    print(family.type)


if __name__ == '__main__':
    search_family(*sys.argv[1:])
