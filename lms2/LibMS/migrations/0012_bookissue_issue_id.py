# Generated by Django 5.1.1 on 2025-02-02 09:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LibMS", "0011_remove_bookissue_iissue_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookissue",
            name="issue_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
