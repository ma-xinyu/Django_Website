# Generated by Django 3.2.6 on 2021-08-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default=1, max_length=100, verbose_name='标题'),
            preserve_default=False,
        ),
    ]