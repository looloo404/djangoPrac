# Generated by Django 4.1.5 on 2023-02-07 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="choice",
            old_name="Question_id",
            new_name="question_id",
        ),
    ]
