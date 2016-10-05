import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maio.settings")

from django.conf import settings


def parse_version(version=None):
    if version is None:
        return (0, 0)
    return tuple(version.split('.'))

def get_version(version=None):
    if version is None:
        version_file = os.path.join(settings.BASE_DIR, 'VERSION.txt')
        with open(version_file, 'r') as fh:
            version = fh.read().strip()
    return parse_version(version)

VERSION = get_version()
