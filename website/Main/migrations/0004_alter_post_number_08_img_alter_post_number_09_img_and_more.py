# Generated by Django 4.1.5 on 2023-02-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_alter_post_child_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_08_img',
            field=models.ImageField(default='parent_cat/1.png', upload_to='thumbnail/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_09_img',
            field=models.ImageField(default='parent_cat/1.png', upload_to='thumbnail/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='number_10_img',
            field=models.ImageField(default='parent_cat/1.png', upload_to='thumbnail/'),
        ),
    ]