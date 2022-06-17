# Generated by Django 4.0.5 on 2022-06-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_info_littype_alter_info_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('littype', models.TextField()),
                ('image', models.FileField(upload_to='app/files/')),
            ],
        ),
    ]
