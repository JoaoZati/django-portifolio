# Generated by Django 3.2.9 on 2021-11-15 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltype',
            name='static_image',
            field=models.TextField(default='source_code_red.jpeg'),
            preserve_default=False,
        ),
    ]