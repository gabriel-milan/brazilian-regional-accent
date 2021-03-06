# Generated by Django 3.2.6 on 2021-08-16 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('radio_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('profession', models.CharField(default='', max_length=255)),
                ('years_on_current_city', models.IntegerField()),
                ('birth_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='birth_city', to='accent_collector.city')),
                ('current_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_city', to='accent_collector.city')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accent_collector.gender')),
                ('parents_original_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents_original_city', to='accent_collector.city')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('audio_file_path', models.CharField(max_length=1023)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accent_collector.sentence')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accent_collector.speaker')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accent_collector.state'),
        ),
    ]
