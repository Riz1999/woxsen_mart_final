# Generated by Django 4.2.1 on 2023-05-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Fashion', 'Fashion'), ('Electronics', 'Electronics'), ('Bikes', 'Bikes'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Jobs', 'Jobs'), ('Cars', 'Cars'), ('Property', 'Property')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('MI', 'Sikkim'), ('PB', 'Punjab'), ('HP', 'Haryana'), ('JH', 'Jharkhand'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('WB', 'West Bengal'), ('BR', 'Bihar'), ('MN', 'Manipur'), ('MH', 'Maharashtra'), ('MZ', 'Mizoram'), ('TR', 'Tripura'), ('TS', 'Telegana'), ('NL', 'Nagaland'), ('GJ', 'Gujarat'), ('AR', 'Arunachal Pradesh'), ('AP', 'Andhra Pradesh'), ('CG', 'Chhattisgarh'), ('KA', 'Karnataka'), ('UP', 'Uttar Pradesh'), ('RJ', 'Rajasthan'), ('TN', 'Tamil Nadu'), ('UK', 'Uttarakhand'), ('OD', 'Odisha'), ('ML', 'Meghalaya'), ('AS', 'Assam'), ('GA', 'Goa')], max_length=100),
        ),
    ]
