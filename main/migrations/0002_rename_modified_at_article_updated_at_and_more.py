# Generated by Django 4.2.5 on 2024-02-28 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='authordetails',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='bookreferenced',
            old_name='modified_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='modified_at',
            new_name='updated_at',
        ),
    ]
