# Generated by Django 3.2.5 on 2022-07-21 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0006_auto_20220721_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='gsentence',
            name='u_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
    ]