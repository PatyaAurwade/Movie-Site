# Generated by Django 5.0.7 on 2024-11-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pratik', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventitem',
            name='imageURL',
            field=models.URLField(default='https://example.com/default-image.jpg', max_length=300),
        ),
    ]
