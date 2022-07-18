# Generated by Django 2.1.4 on 2018-12-25 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import taggit.managers
import wagtail.blocks
import wagtail.fields
import wagtail.models
import wagtail.images.blocks
import wagtail.images.models
import wagtail.search.index
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0002_auto_20150616_2121"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ArticleAuthor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="ArticleAuthorRelationship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                )
            ],
        ),
        migrations.CreateModel(
            name="ArticlePage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("headline", wagtail.fields.RichTextField()),
                ("subdeck", wagtail.fields.RichTextField(blank=True, null=True)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("paragraph", wagtail.blocks.RichTextBlock()),
                            ("image", wagtail.images.blocks.ImageChooserBlock()),
                            (
                                "photo_gallery",
                                wagtail.blocks.ListBlock(
                                    wagtail.snippets.blocks.SnippetChooserBlock(
                                        "core.Photo"
                                    )
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "summary",
                    wagtail.fields.RichTextField(
                        blank=True,
                        help_text="Displayed on the home page or other places to provide a taste of what the article is about.",
                        null=True,
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ArticlesIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Contributor",
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
                ("name", models.CharField(max_length=255)),
                (
                    "article_author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.ArticleAuthor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomImage",
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
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "file",
                    models.ImageField(
                        height_field="height",
                        upload_to=wagtail.images.models.get_upload_to,
                        verbose_name="file",
                        width_field="width",
                    ),
                ),
                ("width", models.IntegerField(editable=False, verbose_name="width")),
                ("height", models.IntegerField(editable=False, verbose_name="height")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="created at"
                    ),
                ),
                ("focal_point_x", models.PositiveIntegerField(blank=True, null=True)),
                ("focal_point_y", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "focal_point_width",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "focal_point_height",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("file_size", models.PositiveIntegerField(editable=False, null=True)),
                (
                    "file_hash",
                    models.CharField(blank=True, editable=False, max_length=40),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        default=wagtail.models.get_root_collection_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Collection",
                        verbose_name="collection",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name="CustomRendition",
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
                ("filter_spec", models.CharField(db_index=True, max_length=255)),
                (
                    "file",
                    models.ImageField(
                        height_field="height",
                        upload_to=wagtail.images.models.get_rendition_upload_to,
                        width_field="width",
                    ),
                ),
                ("width", models.IntegerField(editable=False)),
                ("height", models.IntegerField(editable=False)),
                (
                    "focal_point_key",
                    models.CharField(
                        blank=True, default="", editable=False, max_length=16
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="renditions",
                        to="core.CustomImage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Kicker",
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
                ("title", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MigrationInformation",
            fields=[
                ("link", models.URLField(db_index=True)),
                (
                    "guid",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                (
                    "article",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ArticlePage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("caption", wagtail.fields.RichTextField(blank=True, null=True)),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.CustomImage",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Position",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="StaffIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                )
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StaffPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("biography", wagtail.fields.RichTextField(blank=True, null=True)),
                (
                    "email_address",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "article_author",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.ArticleAuthor",
                    ),
                ),
                (
                    "photo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.CustomImage",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="StaticPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("body", wagtail.fields.RichTextField()),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Term",
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
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("date_started", models.DateField()),
                ("date_ended", models.DateField(blank=True, null=True)),
                (
                    "person",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="terms",
                        to="core.StaffPage",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="terms",
                        to="core.Position",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
        migrations.AddField(
            model_name="customimage",
            name="photographer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="core.StaffPage",
            ),
        ),
        migrations.AddField(
            model_name="customimage",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text=None,
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="tags",
            ),
        ),
        migrations.AddField(
            model_name="customimage",
            name="uploaded_by_user",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="uploaded by user",
            ),
        ),
        migrations.AddField(
            model_name="articlepage",
            name="featured_photo",
            field=models.ForeignKey(
                blank=True,
                help_text="Shown at the top of the article and on the home page.",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.Photo",
            ),
        ),
        migrations.AddField(
            model_name="articlepage",
            name="kicker",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="core.Kicker",
            ),
        ),
        migrations.AddField(
            model_name="articleauthorrelationship",
            name="article",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="authors",
                to="core.ArticlePage",
            ),
        ),
        migrations.AddField(
            model_name="articleauthorrelationship",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="articles",
                to="core.ArticleAuthor",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="customrendition",
            unique_together={("image", "filter_spec", "focal_point_key")},
        ),
        migrations.AlterUniqueTogether(
            name="articleauthorrelationship", unique_together={("article", "author")}
        ),
    ]
