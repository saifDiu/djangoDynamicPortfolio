# Generated by Django 3.1.1 on 2020-09-24 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20200924_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='worksarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planguage', models.CharField(max_length=50, null=True)),
                ('frameworkname', models.CharField(max_length=100, null=True)),
                ('workTitle', models.CharField(max_length=200, null=True)),
                ('workDescription', models.TextField(null=True)),
                ('myProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprofile.myprofile')),
            ],
        ),
        migrations.DeleteModel(
            name='skills',
        ),
    ]