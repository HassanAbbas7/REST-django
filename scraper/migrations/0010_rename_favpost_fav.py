# Generated by Django 4.1.7 on 2023-04-01 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0009_rename_liked_posts_customuser_favourite_posts_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavPost',
            new_name='Fav',
        ),
    ]
