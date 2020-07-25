# Generated by Django 2.2.7 on 2019-11-17 19:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191117_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='step',
            field=models.CharField(default='first_expression', max_length=32),
        ),
        migrations.CreateModel(
            name='CodeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('input', models.TextField()),
                ('output', models.TextField()),
                ('source', models.CharField(max_length=32)),
                ('step', models.CharField(default='first_expression', max_length=32)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='code_entries', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
