# Generated by Django 4.0.3 on 2022-03-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=264)),
                ('profile_pic', models.ImageField(upload_to='img')),
            ],
        ),
    ]
