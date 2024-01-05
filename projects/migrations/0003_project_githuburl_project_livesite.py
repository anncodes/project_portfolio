# Generated by Django 4.2.3 on 2024-01-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='githuburl',
            field=models.URLField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='project',
            name='livesite',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]