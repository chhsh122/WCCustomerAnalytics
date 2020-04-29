# Generated by Django 3.0.5 on 2020-04-26 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='一个文件分类的名字应该唯一', max_length=128, unique=True, verbose_name='文件分类')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '文件分类',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '描述',
                'verbose_name_plural': '数据管理',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.Title')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片管理',
            },
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, help_text='名称', max_length=128, verbose_name='名称')),
                ('gender', models.IntegerField(choices=[(0, '文化娱乐'), (1, '游戏资讯'), (2, '分布式云存储')], default=0, verbose_name='文件分类')),
                ('idCard', models.CharField(blank=True, help_text='SEO描述', max_length=18, null=True, verbose_name='SEO描述')),
                ('phone', models.CharField(max_length=11, verbose_name='官网')),
                ('birthday', models.CharField(max_length=18, verbose_name='SEO标题')),
                ('time', models.TimeField(auto_now=True, verbose_name='时间')),
                ('enable', models.BooleanField(default=True, verbose_name='是否开启')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.Department', verbose_name='顺序')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.Title', verbose_name='业务模式')),
            ],
            options={
                'verbose_name': '云存储',
                'verbose_name_plural': '云存储管理',
            },
        ),
    ]
