# Generated by Django 2.1.2 on 2018-10-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customertable',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='customertable',
            old_name='Email_Id',
            new_name='email_id',
        ),
        migrations.RenameField(
            model_name='customertable',
            old_name='First_Name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='customertable',
            old_name='Last_Name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='customertable',
            old_name='Phone_No',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='movietable',
            old_name='Catogery',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='movietable',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movietable',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='movietable',
            old_name='Released_date',
            new_name='released_date',
        ),
        migrations.RemoveField(
            model_name='customertable',
            name='Address1',
        ),
        migrations.RemoveField(
            model_name='customertable',
            name='Address2',
        ),
        migrations.RemoveField(
            model_name='customertable',
            name='City',
        ),
        migrations.RemoveField(
            model_name='customertable',
            name='Zip_code',
        ),
        migrations.AddField(
            model_name='customertable',
            name='address1',
            field=models.CharField(default=1, max_length=100, verbose_name='Address line 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customertable',
            name='address2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address line 1'),
        ),
        migrations.AddField(
            model_name='customertable',
            name='city',
            field=models.CharField(default=1, max_length=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customertable',
            name='zip_code',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
