# Generated by Django 2.2.2 on 2019-10-03 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191003_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=False),
        ),
    ]
