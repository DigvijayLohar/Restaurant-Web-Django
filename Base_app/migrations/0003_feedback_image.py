# Generated by Django 5.0.7 on 2024-08-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Base_app", "0002_aboutus_feedback_itemlist_alter_book_table1_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="Image",
            field=models.ImageField(default=12, upload_to="Items/"),
            preserve_default=False,
        ),
    ]
