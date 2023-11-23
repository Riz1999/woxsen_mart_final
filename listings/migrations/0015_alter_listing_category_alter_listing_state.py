# Generated by Django 4.2.7 on 2023-11-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_auto_20230526_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Cars', 'Cars'), ('Furniture', 'Furniture'), ('Mobiles', 'Mobiles'), ('Bikes', 'Bikes'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('UK', 'Uttarakhand'), ('BR', 'Bihar'), ('MI', 'Sikkim'), ('JH', 'Jharkhand'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('NL', 'Nagaland'), ('TS', 'Telangana'), ('RJ', 'Rajasthan'), ('WB', 'West Bengal'), ('GJ', 'Gujarat'), ('ML', 'Meghalaya'), ('MN', 'Manipur'), ('HP', 'Haryana'), ('AP', 'Andhra Pradesh'), ('CG', 'Chhattisgarh'), ('KL', 'Kerala'), ('TR', 'Tripura'), ('MZ', 'Mizoram'), ('UP', 'Uttar Pradesh'), ('AS', 'Assam'), ('AR', 'Arunachal Pradesh'), ('PB', 'Punjab'), ('KA', 'Karnataka'), ('TN', 'Tamil Nadu'), ('GA', 'Goa'), ('OD', 'Odisha')], max_length=100),
        ),
    ]
