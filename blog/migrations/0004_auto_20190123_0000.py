# Generated by Django 2.1.5 on 2019-01-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190122_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mark',
            field=models.CharField(choices=[('1', 'Terrible'), ('2', 'Bad'), ('3', 'Neutral'), ('4', 'Good'), ('5', 'Perfect')], max_length=20, null=True, verbose_name='Mark'),
        ),
    ]