# Generated by Django 4.2.10 on 2024-03-05 11:22
import warnings

from django.db import migrations, models


def print_warning_for_initializing_manifest_data(apps, schema_editor):
    warnings.warn(
        "Run 'pulpcore-manager container-handle-image-data' to move the manifests' "
        "data from artifacts to the new 'data' database field."
    )


class Migration(migrations.Migration):

    dependencies = [
        ("container", "0038_add_manifest_metadata_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="manifest",
            name="data",
            field=models.TextField(null=True),
        ),
        migrations.RunPython(
            print_warning_for_initializing_manifest_data,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
    ]
