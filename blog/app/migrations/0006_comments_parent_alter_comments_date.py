# Generated by Django 4.2.4 on 2023-08-14 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='replies', to='app.comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
