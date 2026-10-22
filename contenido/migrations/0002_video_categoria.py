from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenido", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("naranon", "Material Nar-Anon"),
                    ("musicales", "Musicales"),
                    ("peliculas", "Películas"),
                ],
                db_index=True,
                default="naranon",
                max_length=20,
            ),
        ),
    ]
