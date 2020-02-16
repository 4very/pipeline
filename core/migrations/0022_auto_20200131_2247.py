# Generated by Django 2.2.9 on 2020-01-31 22:47

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [("core", "0021_officesorderable_electionpage")]

    operations = [
        migrations.CreateModel(
            name="NomCount",
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
                ("count", models.IntegerField(default=0)),
                (
                    "office",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="core.Office"
                    ),
                ),
            ],
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.RemoveField(model_name="officesorderable", name="page"),
        migrations.CreateModel(
            name="NomCountOrderable",
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
                (
                    "NomCount",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.NomCount"
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nom_counts",
                        to="core.CandidatePage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False},
        ),
    ]