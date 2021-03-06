# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-13 11:20
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('key', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True, verbose_name='Date')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='AdminNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(default=False, verbose_name='Is ')),
                ('priority', models.IntegerField(blank=True, default=4, null=True, verbose_name='Priority')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutPromoCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promo_code', models.CharField(max_length=15, null=True, verbose_name='Promo code')),
                ('percent', models.FloatField(null=True, verbose_name='Discount percent')),
                ('qty', models.IntegerField(null=True, verbose_name='Quantity of codes')),
                ('date_from', models.DateField(null=True, verbose_name='Date from')),
                ('date_till', models.DateField(null=True, verbose_name='Date till')),
                ('used_by', models.ManyToManyField(blank=True, related_name='used_coupons', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Company name')),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Company street')),
                ('city', models.CharField(default='Barcelona', max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(default='Catalonia', max_length=30, null=True, verbose_name='State full')),
                ('zip_code', models.CharField(max_length=10, null=True, verbose_name='Zip Code')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='Office Phone Number')),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='Office is confirmed?')),
            ],
        ),
        migrations.CreateModel(
            name='Lunchbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name of lunchbox')),
                ('desc', models.TextField(null=True, verbose_name='Description')),
                ('price', models.FloatField(null=True, verbose_name='Price')),
                ('available_from', models.DateField(null=True, verbose_name='Available from')),
                ('available_till', models.DateField(null=True, verbose_name='Available till')),
                ('protein', models.IntegerField(blank=True, null=True, verbose_name='Protein (Gr)')),
                ('carbohydrates', models.IntegerField(blank=True, null=True, verbose_name='Carbohydrates (Gr)')),
                ('fat', models.IntegerField(blank=True, null=True, verbose_name='Fat (Gr)')),
                ('sugar', models.IntegerField(blank=True, null=True, verbose_name='Sugar (Gr)')),
                ('sodium', models.IntegerField(blank=True, null=True, verbose_name='Sodium (Mgr)')),
                ('published', models.BooleanField(default=False, verbose_name='Published?')),
                ('photoshoot_requested', models.BooleanField(default=False, verbose_name='Photoshoot requested?')),
                ('publishing_requested', models.BooleanField(default=False, verbose_name='Published requested?')),
                ('date', models.DateTimeField(auto_now=True, null=True, verbose_name='Last saved date')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='La Fiambrera rate')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxAdminMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=255, null=True, verbose_name='Admin message')),
                ('inc', models.BooleanField(default=True, verbose_name='Incoming?')),
                ('watched', models.BooleanField(default=False, verbose_name='Watched?')),
                ('priority', models.IntegerField(blank=True, default=4, null=True, verbose_name='Priority')),
                ('date', models.DateTimeField(auto_now=True, null=True, verbose_name='Date')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.FloatField(null=True, verbose_name='Discount percent')),
                ('qty', models.IntegerField(null=True, verbose_name='Discount qty')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=255, null=True, verbose_name='Message')),
                ('inc', models.BooleanField(default=True, verbose_name='Incoming?')),
                ('watched', models.BooleanField(default=False, verbose_name='Watched?')),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and time')),
                ('priority', models.IntegerField(blank=True, default=4, null=True, verbose_name='Priority')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('lunchbox', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxPrivileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Lunchbox privilege',
                'verbose_name_plural': 'Lunchbox Privileges',
            },
        ),
        migrations.CreateModel(
            name='LunchboxPrivilegesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
                ('privilege', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.LunchboxPrivileges', verbose_name='Privilege')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(null=True, verbose_name='Rating')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='LunchboxRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lunchbox', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False, verbose_name='Watched?')),
                ('priority', models.IntegerField(blank=True, default=4, null=True, verbose_name='Priority')),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OrderItem', verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Phone Number')),
                ('c_first_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Catering First name')),
                ('c_last_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Catering Last name')),
                ('c_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Catering address')),
                ('c_city', models.CharField(blank=True, default='Barcelona', max_length=50, null=True, verbose_name='Catering city')),
                ('c_state', models.CharField(blank=True, default='Catalonia', max_length=30, null=True, verbose_name='Catering State full')),
                ('c_zip_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Catering Zip Code')),
                ('lang', models.CharField(blank=True, default='en', max_length=2, null=True, verbose_name='Prefered language')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Company', verbose_name='Company')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='', verbose_name='Restaurant logo')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name of restaurant')),
                ('desc', models.TextField(null=True, verbose_name='Short description')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Address')),
                ('city', models.CharField(default='Barcelona', max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(default='Catalonia', max_length=50, null=True, verbose_name='State')),
                ('zip_code', models.CharField(max_length=30, null=True, verbose_name='Zip code')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='Phone Number')),
                ('min_order', models.IntegerField(blank=True, default=1, null=True, verbose_name='Minimal Order')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name', unique_with=['name'], verbose_name='Slug')),
                ('photoshoot_requested', models.BooleanField(default=False, verbose_name='Photoshoot requested?')),
                ('publishing_requested', models.BooleanField(default=False, verbose_name='Published requested?')),
                ('published', models.BooleanField(default=False, verbose_name='Published?')),
                ('rate', models.FloatField(default=10.0, null=True, verbose_name='Restaurant rate %')),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='Is confirmed?')),
                ('is_premium', models.BooleanField(default=False, verbose_name='Is premium account?')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User account')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='Contract text')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possible', models.BooleanField(default=False, verbose_name='Delivery is possible?')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.City', verbose_name='City')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantDiscountCoupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_from', models.DateField(null=True, verbose_name='Available from')),
                ('available_till', models.DateField(null=True, verbose_name='Available till')),
                ('time_from', models.TimeField(null=True, verbose_name='Time from')),
                ('time_till', models.TimeField(null=True, verbose_name='Time till')),
                ('discount_text', models.CharField(blank=True, max_length=50, null=True, verbose_name='Discount text')),
                ('percent', models.IntegerField(blank=True, null=True, verbose_name='Percent')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=255, null=True, verbose_name='Message')),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and time')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(verbose_name='Rating')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='Order')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=3)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('restaurant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='userprofiles.Restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='lunchboxfeedback',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant'),
        ),
        migrations.AddField(
            model_name='lunchboxfeedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='lunchbox',
            name='restaurant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant'),
        ),
        migrations.AddField(
            model_name='adminnotification',
            name='lunchbox',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Lunchbox', verbose_name='Lunchbox'),
        ),
        migrations.AddField(
            model_name='adminnotification',
            name='restaurant',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofiles.Restaurant', verbose_name='Restaurant'),
        ),
    ]
