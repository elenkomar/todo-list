
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField()),
                ("mark", models.BooleanField()),
                (
                    "tags",
                    models.ManyToManyField(related_name="tasks", to="service.tag"),
                ),
            ],
            options={
                "ordering": ["mark", "datetime"],
            },
        ),
    ]
