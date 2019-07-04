# Generated by Django 2.0.8 on 2019-07-03 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dong', models.CharField(blank=True, choices=[('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'), ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'), ('115', '115'), ('116', '116'), ('117', '117'), ('118', '118'), ('119', '119')], max_length=3)),
                ('ho', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=15)),
                ('tel1', models.PositiveSmallIntegerField()),
                ('tel2', models.PositiveSmallIntegerField()),
                ('tel3', models.PositiveSmallIntegerField()),
                ('voting', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='VoteSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('text', models.TextField(blank=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('whose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='vote',
            name='which',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='mainapp.VoteSubject'),
        ),
    ]
