# Generated by Django 2.2.1 on 2019-07-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0012_auto_20190716_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordergoods',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上传时间'),
        ),
    ]
