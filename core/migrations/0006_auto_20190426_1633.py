# Generated by Django 2.1.8 on 2019-04-26 16:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [("core", "0005_auto_20181225_2103")]

    operations = [
        migrations.AlterField(
            model_name="articlepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    ("image", wagtail.images.blocks.ImageChooserBlock()),
                    (
                        "photo_gallery",
                        wagtail.blocks.ListBlock(
                            wagtail.snippets.blocks.SnippetChooserBlock("core.Photo"),
                            icon="image",
                        ),
                    ),
                    (
                        "embed",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "embed",
                                    wagtail.embeds.blocks.EmbedBlock(
                                        help_text="URL to the content to embed."
                                    ),
                                )
                            ]
                        ),
                    ),
                ]
            ),
        )
    ]
