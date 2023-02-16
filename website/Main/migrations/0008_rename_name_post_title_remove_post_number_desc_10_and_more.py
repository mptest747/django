# Generated by Django 4.1.5 on 2023-02-06 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_alter_post_number_img_10'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_desc_10',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_desc_8',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_desc_9',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_img_10',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_img_8',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_img_9',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_title_10',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_title_8',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_title_9',
        ),
        migrations.CreateModel(
            name='DetailPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_title_10', models.CharField(default='', max_length=100)),
                ('number_img_10', models.ImageField(default='parent_cat/1.png', upload_to='thumbnail/')),
                ('number_desc_10', models.CharField(default='', max_length=500)),
                ('number_title_9', models.CharField(default='', max_length=100)),
                ('number_img_9', models.ImageField(default='parent_cat/1.png', upload_to='parent_cat/')),
                ('number_desc_9', models.CharField(default='', max_length=500)),
                ('number_title_8', models.CharField(default='', max_length=100)),
                ('number_img_8', models.ImageField(default='parent_cat/1.png', upload_to='parent_cat/')),
                ('number_desc_8', models.CharField(default='', max_length=500)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.post')),
            ],
        ),
    ]
