# Generated by Django 5.0.1 on 2024-01-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('posts', models.ManyToManyField(blank=True, related_name='tags', to='posts.post')),
            ],
        ),
    ]
