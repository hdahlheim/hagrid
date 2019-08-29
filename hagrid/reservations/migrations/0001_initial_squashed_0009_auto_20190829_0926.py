# Generated by Django 2.2.4 on 2019-08-29 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('reservations', '0001_initial'), ('reservations', '0002_auto_20190825_1919'), ('reservations', '0003_auto_20190825_1931'), ('reservations', '0004_auto_20190825_1958'), ('reservations', '0005_auto_20190826_1207'), ('reservations', '0006_auto_20190826_1526'), ('reservations', '0007_auto_20190826_2300'), ('reservations', '0008_auto_20190828_1153'), ('reservations', '0009_auto_20190829_0926')]

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_mail', models.EmailField(blank=True, max_length=254)),
                ('contact_dect', models.CharField(blank=True, max_length=10)),
                ('secret', models.CharField(max_length=16, unique=True)),
                ('state', models.CharField(choices=[('unapproved', 'unapproved'), ('editable', 'editable'), ('submitted', 'submitted'), ('packed', 'packed'), ('ready for pickup', 'ready to be picked up'), ('picked up', 'picked up'), ('canceled', 'cancelled')], default='unapproved', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='reservations.Reservation')),
                ('title', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=0)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='reservations.ReservationPart')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Variation')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_state', models.CharField(choices=[('unapproved', 'unapproved'), ('editable', 'editable'), ('submitted', 'submitted'), ('packed', 'packed'), ('ready for pickup', 'ready to be picked up'), ('picked up', 'picked up'), ('canceled', 'cancelled')], max_length=20)),
                ('new_state', models.CharField(choices=[('unapproved', 'unapproved'), ('editable', 'editable'), ('submitted', 'submitted'), ('packed', 'packed'), ('ready for pickup', 'ready to be picked up'), ('picked up', 'picked up'), ('canceled', 'cancelled')], max_length=20)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='reservations.Reservation')),
            ],
        ),
    ]