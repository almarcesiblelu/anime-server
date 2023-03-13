from django.core.management.base import BaseCommand, CommandError
from anime.models import Anime
import csv

# is this the best way to import ?


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('anime_file', type=str)

    def handle(self, *args, **options):
        anime_file = options['anime_file']
        with open(anime_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                anime = Anime(
                    name=row['name'],
                    genre=row['genre'],
                    type=row['type'],
                    episodes=row['episodes'],
                    rating=row['rating'],
                    members=row['members'],
                )
                anime.save()
        # fix this crap
        self.stdout.write(self.style.SUCCESS('import_anime sucess'))
