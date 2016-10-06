from django.core.management.base import BaseCommand, CommandError

class MaioBaseCommand(BaseCommand):
    args = '<None>'
    help = 'Extend MaioBaseCommand into a Command class to create a command for use in manage.py'
    can_import_settings = True

    def out(self, *args, **kwargs):
        self.stdout.write(' '.join(args))

