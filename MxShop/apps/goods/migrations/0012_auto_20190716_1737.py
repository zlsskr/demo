# Generated by Django 2.2.1 on 2019-07-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20190716_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='hotsearchwords',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='添加时间'),
        ),
    ]
