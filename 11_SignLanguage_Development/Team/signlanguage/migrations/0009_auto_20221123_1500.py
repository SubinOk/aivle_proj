# Generated by Django 3.2 on 2022-11-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0008_result_equal'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ai_file', models.FileField(blank=True, upload_to='')),
                ('version', models.CharField(max_length=100)),
                ('is_selected', models.BooleanField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='ModelCnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100)),
                ('equal', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='result',
            name='equal',
        ),
    ]
