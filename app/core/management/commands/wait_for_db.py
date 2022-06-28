"""
Django command to wait for db availability
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waiting for database...')  # its showing message during execute
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, wait...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
