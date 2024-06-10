# Generated by Django 5.0.6 on 2024-06-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seirs_sim', '0002_simulationparameters_imm_boost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simulationparameters',
            old_name='prob',
            new_name='rel_beta_inf',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='dt',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='end',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='start',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='timestep',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='use_vaccine',
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='dur_exp_inf',
            field=models.FloatField(default=2.0),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='dur_exp_rec',
            field=models.FloatField(default=2.0),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='dur_inf',
            field=models.FloatField(default=14.0),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='dur_rec',
            field=models.FloatField(default=7.0),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='init_prev',
            field=models.FloatField(default=0.005),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='p_death',
            field=models.FloatField(default=0.05),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='p_symptoms',
            field=models.FloatField(default=0.4),
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='waning',
            field=models.FloatField(default=0.0009132420091324201),
        ),
        migrations.AlterField(
            model_name='simulationparameters',
            name='beta',
            field=models.FloatField(default=0.08),
        ),
        migrations.AlterField(
            model_name='simulationparameters',
            name='imm_boost',
            field=models.FloatField(default=0.001),
        ),
    ]
