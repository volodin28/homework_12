from django.core.management.base import BaseCommand
from faker import Faker
from article.models import Article

faker = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("quantity", type=int, nargs="?", default=1)

    def handle(self, quantity, **options):
        for _ in range(quantity):
            a = Article.objects.create(
                title=faker.name(), content=faker.paragraph(nb_sentences=5)
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully created article with ID "%s"' % a.id)
            )
