# Generated by Django 4.1.3 on 2023-02-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0003_remove_message_text_message_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.CharField(blank=True, default='09/02/2023 00:20:46', max_length=1000, verbose_name='Дата отправки сообщения'),
        ),
    ]
