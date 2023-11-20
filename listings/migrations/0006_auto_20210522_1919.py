# Generated by Django 3.1.7 on 2021-05-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20210522_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Property', 'Property'), ('Furniture', 'Furniture'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Books&Sports', 'Books&Sports'), ('Bikes', 'Bikes'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('MH', 'Maharashtra'), ('ML', 'Meghalaya'), ('RJ', 'Rajasthan'), ('GA', 'Goa'), ('JH', 'Jharkhand'), ('HP', 'Haryana'), ('UP', 'Uttar Pradesh'), ('TS', 'Telegana'), ('OD', 'Odisha'), ('BR', 'Bihar'), ('PB', 'Punjab'), ('TR', 'Tripura'), ('TN', 'Tamil Nadu'), ('WB', 'West Bengal'), ('MN', 'Manipur'), ('UK', 'Uttarakhand'), ('KA', 'Karnataka'), ('MP', 'Madhya Pradesh'), ('GJ', 'Gujarat'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('MZ', 'Mizoram'), ('AR', 'Arunachal Pradesh'), ('MI', 'Sikkim'), ('NL', 'Nagaland'), ('AS', 'Assam'), ('CG', 'Chhattisgarh')], max_length=100),
        ),
    ]
