# Generated by Django 2.0.9 on 2018-11-21 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181121_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
