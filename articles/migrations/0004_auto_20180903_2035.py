# Generated by Django 2.0.8 on 2018-09-03 20:35

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [("articles", "0003_auto_20180903_1816")]

    operations = [
        migrations.AlterField(
            model_name="articleauthorrelationship",
            name="article",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="authors",
                to="articles.ArticlePage",
            ),
        )
    ]