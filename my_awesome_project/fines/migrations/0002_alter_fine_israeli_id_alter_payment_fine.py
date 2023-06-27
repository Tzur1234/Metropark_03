# Generated by Django 4.1.9 on 2023-06-27 10:23

from django.db import migrations, models
import django.db.models.deletion
import my_awesome_project.fines.models


class Migration(migrations.Migration):
    dependencies = [
        ("fines", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fine",
            name="israeli_id",
            field=my_awesome_project.fines.models.CardIDField(default=111111111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="payment",
            name="fine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="payments", to="fines.fine"
            ),
        ),
    ]
