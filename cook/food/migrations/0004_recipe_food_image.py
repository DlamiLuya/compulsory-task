# Generated by Django 4.2.4 on 2023-08-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_recipe_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
