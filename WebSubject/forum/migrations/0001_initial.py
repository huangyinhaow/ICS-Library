# Generated by Django 4.0.4 on 2022-05-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_id', models.CharField(max_length=20, unique=True, verbose_name='组织ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_tid', models.CharField(max_length=16, verbose_name='帖子id')),
                ('r_uid', models.CharField(max_length=16, verbose_name='发表者id')),
                ('r_photo', models.CharField(max_length=128, null=True, verbose_name='回复的图片')),
                ('r_time', models.DateField(auto_now_add=True, verbose_name='留言时间')),
                ('r_content', models.CharField(max_length=256, verbose_name='回复内容')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_uid', models.CharField(max_length=16, verbose_name='帖子所属用户id')),
                ('t_kind', models.CharField(max_length=32, verbose_name='类别')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('t_photo', models.CharField(max_length=128, null=True, verbose_name='帖子图片')),
                ('t_content', models.CharField(max_length=3000, verbose_name='帖子正文')),
                ('t_title', models.CharField(max_length=64, verbose_name='帖子标题')),
                ('t_introduce', models.CharField(max_length=256, verbose_name='帖子简介')),
                ('recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.IntegerField(verbose_name='板块编号')),
                ('number', models.IntegerField(verbose_name='在该板块的编号')),
                ('r_text', models.TextField(verbose_name='推荐语')),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='书籍ID')),
            ],
        ),
    ]
