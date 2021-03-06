# Generated by Django 2.2.3 on 2019-09-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_post_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_img',
        ),
        migrations.CreateModel(
            name='PostBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(default='default_post_img.jpg', upload_to='post_images')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
