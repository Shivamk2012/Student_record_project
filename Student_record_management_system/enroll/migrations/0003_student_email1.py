# Generated by Django 4.1.3 on 2023-02-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_alter_student_mob'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email1',
            field=models.EmailField(default='email@gmail.com', max_length=254, unique=True),
        ),
    ]