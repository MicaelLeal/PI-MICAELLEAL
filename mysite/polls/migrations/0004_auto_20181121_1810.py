# Generated by Django 2.0.9 on 2018-11-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181121_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
