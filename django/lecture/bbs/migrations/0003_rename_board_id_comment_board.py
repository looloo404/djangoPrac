# Generated by Django 4.1.5 on 2023-02-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bbs", "0002_rename_board_comment_board_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="board_id",
            new_name="board",
        ),
    ]
