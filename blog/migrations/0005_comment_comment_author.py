# Generated by Django 4.2.3 on 2023-07-24 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment_comment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
