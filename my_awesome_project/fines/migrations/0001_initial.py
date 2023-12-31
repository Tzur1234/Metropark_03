# Generated by Django 4.1.9 on 2023-06-26 20:46

from django.db import migrations, models
import django.db.models.deletion
import my_awesome_project.fines.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fine",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("israeli_id", my_awesome_project.fines.models.CardIDField(blank=True, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(choices=[("O", "Open"), ("C", "Close")], max_length=1)),
                ("description", models.TextField()),
                ("amount_in_pennies", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.CharField(choices=[("1", "Cash"), ("2", "Credit Card"), ("3", "Check")], max_length=1),
                ),
                ("amount_in_pennies", models.PositiveIntegerField()),
                (
                    "fine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="fines", to="fines.fine"
                    ),
                ),
            ],
        ),
    ]
