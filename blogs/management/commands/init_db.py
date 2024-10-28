import random
import tqdm
from django.core.management.base import BaseCommand
from blogs.models import Blog
from django.contrib.auth import get_user_model

User = get_user_model()
PASSWORD =  "abcd1234"

class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.all().delete()
        Blog.objects.all().delete()

        User.objects.create_superuser(username="admin", password="1234")
        
        users = []
        for i in tqdm.tqdm(range(1, 11), "users"):
            user = User.objects.create_user(username=f"user{i}", password=PASSWORD)
            users.append(user)
        
        for i in tqdm.tqdm(range(1, 21), "blogs"):
            blog = Blog.objects.create(
                title=f"title{i}",
                text=f"text{i}",
                author=random.choice(users),
                status=random.choice(['drf', 'pub']),
            )

