# Generated by Django 4.1.5 on 2023-02-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_alter_post_number_img_10_alter_post_number_img_8_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='number_img_10',
            field=models.ImageField(default='parent_cat/1.png', upload_to='thumbnail/'),
        ),
    ]
