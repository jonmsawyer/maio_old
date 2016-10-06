from random import choice
from string import printable

from django.core.management.base import CommandError

from maio.management.commands._base import MaioBaseCommand


class Command(MaioBaseCommand):
    args = '<None>'
    help = 'Generates a pseudorandom SECRET_KEY for use in conf/site_settings.py'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('num_chars', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        num_chars = int(kwargs.get('num_chars', 50))
        self.out("SECRET_KEY = '%s'" % (''.join([choice(printable[:-6]) for x in xrange(0, int(num_chars))]).replace("'", "\\'"),))
