# Generated by Django 2.0.9 on 2018-11-13 17:37

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [("newsletter", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                (
                    "body",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "article",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "article",
                                            wagtail.core.blocks.PageChooserBlock(
                                                target_model=["articles.ArticlePage"]
                                            ),
                                        ),
                                        (
                                            "headline",
                                            wagtail.core.blocks.RichTextBlock(
                                                help_text="Optional. Will override the article's headline.",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "summary",
                                            wagtail.core.blocks.RichTextBlock(
                                                help_text="Optional. Will override the article's summary.",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ("text", wagtail.core.blocks.RichTextBlock()),
                        ]
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]