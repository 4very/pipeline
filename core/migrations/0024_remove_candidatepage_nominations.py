# Generated by Django 2.2.9 on 2020-02-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("core", "0023_auto_20200201_2030")]

    operations = [
        migrations.RemoveField(model_name="candidatepage", name="nominations")
    ]