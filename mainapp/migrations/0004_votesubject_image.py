# Generated by Django 2.0.8 on 2019-07-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_votesubject_stater'),
    ]

    operations = [
        migrations.AddField(
            model_name='votesubject',
            name='image',
            field=models.ImageField(blank=True, upload_to='gong_go/image'),
        ),
    ]
