# Generated by Django 2.2.10 on 2022-03-15 23:00

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20220315_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('photo', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock(features=['italic'], required=False)), ('size', wagtail.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Width of image in article.'))])), ('photo_gallery', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock(features=['italic'], required=False))]), icon='image')), ('embed', wagtail.blocks.StructBlock([('embed', wagtail.embeds.blocks.EmbedBlock(help_text='URL to the content to embed.')), ('size', wagtail.blocks.ChoiceBlock(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], help_text='Width of video in article.'))])), ('carousel', wagtail.blocks.StreamBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.RichTextBlock(features=['italic'], required=False))]))], blank=True),
        ),
    ]
