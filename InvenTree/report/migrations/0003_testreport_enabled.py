# Generated by Django 3.0.7 on 2020-08-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_delete_reporttemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='testreport',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Report template is enabled', verbose_name='Enabled'),
        ),
    ]