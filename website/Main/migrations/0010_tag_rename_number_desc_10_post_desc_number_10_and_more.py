# Generated by Django 4.1.5 on 2023-02-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_rename_title_post_name_post_number_desc_10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='number_desc_10',
            new_name='desc_number_10',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='number_desc_8',
            new_name='desc_number_8',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='number_desc_9',
            new_name='desc_number_9',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='number_title_10',
            new_name='title_number_10',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='number_title_8',
            new_name='title_number_8',
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
            name='number_title_9',
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_3',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_4',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_5',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_6',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='desc_number_7',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_1',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_10',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_2',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_3',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_4',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_5',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_6',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_7',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_8',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_number_9',
            field=models.ImageField(default='post_images/default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='is_affiliate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_4',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_5',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_6',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_7',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='title_number_9',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Reviewd'), (2, 'Published')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='Main.tag'),
        ),
    ]
