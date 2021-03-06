# Generated by Django 3.2 on 2021-04-21 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('communication_id', models.AutoField(primary_key=True, serialize=False)),
                ('communication_title', models.CharField(max_length=250)),
                ('communication_content', models.TextField()),
                ('communication_img', models.CharField(max_length=250, null=True)),
                ('communication_date', models.DateTimeField(auto_now=True)),
                ('communication_views', models.IntegerField(default=0)),
                ('communication_category', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Communication_Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('communication_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.communication')),
            ],
        ),
    ]
