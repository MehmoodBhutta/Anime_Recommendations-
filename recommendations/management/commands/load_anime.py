import pandas as pd
from django.core.management.base import BaseCommand
from recommendations.models import Anime

class Command(BaseCommand):
    help = 'Load anime data from CSV'

    def handle(self, *args, **kwargs):
        # Use absolute path to the CSV file
        csv_path = '/Users/mac/Desktop/Django Project /anime_recommendation/recommendations/data/anime.csv'
        df = pd.read_csv(csv_path)

        for _, row in df.iterrows():
            # Check if the anime_id already exists
            if not Anime.objects.filter(anime_id=row['anime_id']).exists():
                try:
                    rating = float(row['rating']) if row['rating'] != 'Unknown' else None
                except ValueError:
                    rating = None

                episodes = int(row['episodes']) if row['episodes'].isdigit() else None

                Anime.objects.create(
                    anime_id=row['anime_id'],
                    name=row['name'],
                    genre=row['genre'],
                    type=row['type'],
                    episodes=episodes,
                    rating=rating,
                    members=row['members']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded anime data'))