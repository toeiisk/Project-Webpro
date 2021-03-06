# Generated by Django 3.0.4 on 2020-03-05 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_home', '0005_delete_restaurantfood'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_home.Food')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_home.Restaurant')),
            ],
        ),
    ]
