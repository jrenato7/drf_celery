# Generated by Django 3.2.12 on 2022-04-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_eye', '0002_auto_20220403_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.TextField()),
                ('errors', models.TextField(null=True)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
