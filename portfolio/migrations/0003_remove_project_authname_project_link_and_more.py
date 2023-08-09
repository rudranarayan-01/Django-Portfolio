# Generated by Django 4.1 on 2023-08-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_delete_blogs_delete_internship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='authname',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=100000000000000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio'),
        ),
    ]
