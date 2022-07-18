# Generated by Django 2.2.10 on 2022-03-15 14:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191106_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured_articles',
            field=wagtail.fields.StreamField([('one_column', wagtail.blocks.StructBlock([('column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))]))])), ('one_ad_column', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image should be 22:7')), ('link', wagtail.blocks.URLBlock(label='target', required=False))])), ('two_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))])), ('right_column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))])), ('emphasize_column', wagtail.blocks.ChoiceBlock(choices=[('left', 'Left'), ('right', 'Right')], help_text='Which article, if either, should appear larger.', required=False))])), ('three_columns', wagtail.blocks.StructBlock([('left_column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))])), ('middle_column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))])), ('right_column', wagtail.blocks.StructBlock([('article', wagtail.blocks.PageChooserBlock(page_type=['core.ArticlePage'])), ('headline', wagtail.blocks.RichTextBlock(help_text="Optional. Will override the article's headline.", required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional. Ovverides the image on the post.', required=False))]))])), ('recent_articles', wagtail.blocks.StructBlock([('num_articles', wagtail.blocks.IntegerBlock(help_text='Number of recent articles to display.', label='Number of articles'))])), ('marquee_banner', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True)), ('banner_type', wagtail.blocks.ChoiceBlock(choices=[('moves', 'Rotating')], help_text='Determines whether the marquee banner is stationary or rotating. Only rotating works right now.'))]))], null=True),
        ),
    ]
