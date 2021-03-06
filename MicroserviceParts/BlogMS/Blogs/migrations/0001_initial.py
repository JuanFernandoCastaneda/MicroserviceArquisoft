# Generated by Django 3.1.3 on 2020-11-29 15:36

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('created', models.DateField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=50)),
                ('user_id', models.TextField(default=None)),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('created', models.DateField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.TextField(default=None)),
                ('comment', models.CharField(default=None, max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('created', models.DateField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=50)),
                ('content', models.TextField(default=None)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogs.blog')),
            ],
        ),
        migrations.CreateModel(
            name='CommentOfComment',
            fields=[
                ('created', models.DateField(auto_created=True)),
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('user_id', models.TextField(default=None)),
                ('commentOfComment', models.CharField(default=None, max_length=200)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogs.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogs.post'),
        ),
    ]
