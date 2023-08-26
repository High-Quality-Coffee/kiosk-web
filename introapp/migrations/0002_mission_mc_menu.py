
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission_mc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introapp.mission_mc')),
            ],
        ),
    ]