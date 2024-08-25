# Generated by Django 5.0.7 on 2024-07-30 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Base_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aboutus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("User_name", models.CharField(max_length=15)),
                ("Description", models.TextField()),
                ("Ratings", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ItemList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Category_Name", models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name="book_table1",
            name="Date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="book_table1",
            name="Number",
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name="Items",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Item_name", models.CharField(max_length=15)),
                ("Description", models.TextField()),
                ("Price", models.IntegerField()),
                ("Image", models.ImageField(upload_to="Items/")),
                (
                    "Category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Category_name",
                        to="Base_app.itemlist",
                    ),
                ),
            ],
        ),
    ]