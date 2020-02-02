# Generated by Django 2.2.9 on 2020-02-02 03:29

import core.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_electionindexpage_panels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionindexpage',
            name='panels',
            field=wagtail.core.fields.StreamField([('three_cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.StructBlock([('office', wagtail.snippets.blocks.SnippetChooserBlock(core.models.Office))]))]))], null=True),
        ),
    ]
