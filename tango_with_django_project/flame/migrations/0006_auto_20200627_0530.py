# Generated by Django 3.0.7 on 2020-06-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flame', '0005_auto_20200626_0610'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.AddField(
            model_name='deal',
            name='feature',
            field=models.CharField(choices=[('HotDeals', 'Hot Deals'), ('HuoOnly', 'Huozhezi Only'), ('Trending', 'Trending Deals'), ('GoodDeals', 'Good Deals')], default='GoodDeals', max_length=10),
        ),
        migrations.AddField(
            model_name='deal',
            name='not_delated',
            field=models.BooleanField(default=True),
        ),
    ]
