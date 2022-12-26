# Generated by Django 4.1.3 on 2022-12-26 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("my_library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("O", "On_loan"),
                            ("A", "Available"),
                            ("R", "Reserved"),
                            ("C", "Currently_reading"),
                            ("N", "Next_in_line"),
                            ("D", "Done_reading"),
                        ],
                        help_text="Book availability",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="my_library.status",
                verbose_name="books",
            ),
        ),
    ]