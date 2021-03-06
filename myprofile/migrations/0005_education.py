# Generated by Django 3.1.1 on 2020-09-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0004_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200, null=True)),
                ('degreeTitle', models.CharField(max_length=200, null=True)),
                ('institution', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('result', models.FloatField(null=True)),
                ('myProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.myprofile')),
            ],
        ),
    ]
