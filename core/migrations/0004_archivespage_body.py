# Generated by Django 2.2.1 on 2019-05-11 15:30

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("core", "0003_auto_20190511_0230")]

    operations = [
        migrations.AddField(
            model_name="archivespage",
            name="body",
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        )
    ]
