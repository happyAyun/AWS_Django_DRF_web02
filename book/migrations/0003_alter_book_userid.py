# Generated by Django 3.2 on 2021-04-23 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('book', '0002_rename_book_id_book_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]