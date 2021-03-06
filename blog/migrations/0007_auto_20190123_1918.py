# Generated by Django 2.1.5 on 2019-01-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190123_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marks', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='marks', to='blog.User'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='mark',
        ),
        migrations.AddField(
            model_name='post',
            name='mark',
            field=models.ManyToManyField(blank=True, null=True, related_name='post', through='blog.Mark', to='blog.User'),
        ),
    ]
