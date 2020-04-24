# Generated by Django 3.0.5 on 2020-04-24 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0003_auto_20200423_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Link')),
                ('in_reply_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='links.Comment')),
            ],
        ),
    ]