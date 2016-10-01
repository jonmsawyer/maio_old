from random import choice
from string import printable

from django.core.management.base import BaseCommand, CommandError

class MaioBaseCommand(BaseCommand):
    args = '<None>'
    help = 'Extend MaioBaseCommand into a Command class to create a command for use in manage.py'

    def _print(self, *args, **kwargs):
        self.stdout.write(' '.join(args))

class Command(MaioBaseCommand):
    args = '<None>'
    help = 'Generates a pseudorandom SECRET_KEY for use in conf/site_settings.py'

    def handle(self, num_chars=50, *args, **kwargs):
        self._print("SECRET_KEY = '%s'" % (''.join([choice(printable[:-6]) for x in xrange(0, int(num_chars))]).replace("'", "\\'"),))
