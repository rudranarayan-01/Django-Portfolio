# Generated by Django 4.1 on 2023-08-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_project_authname_project_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='portfolio'),
        ),
    ]
