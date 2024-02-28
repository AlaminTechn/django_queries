# Generated by Django 4.2.5 on 2024-02-28 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField(blank=True, max_length=1000, null=True)),
                ('publication_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=55, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('biography', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Author',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('book_title', models.CharField(blank=True, max_length=55)),
                ('publication_date', models.DateTimeField(blank=True, null=True)),
                ('ISBN', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity_available', models.IntegerField(blank=True, default='0', null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('shelf_number', models.CharField(blank=True, max_length=255, null=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
            options={
                'verbose_name_plural': 'Libraries',
                'db_table': 'library',
            },
        ),
        migrations.CreateModel(
            name='BookReferenced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.article')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
            options={
                'verbose_name_plural': 'Books Referenced',
                'db_table': 'book_referenced',
            },
        ),
        migrations.CreateModel(
            name='AuthorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=55, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
            options={
                'verbose_name_plural': 'Author Details',
                'db_table': 'author_details',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.author'),
        ),
    ]