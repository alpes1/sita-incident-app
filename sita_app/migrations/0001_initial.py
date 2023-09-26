# Generated by Django 4.2.5 on 2023-09-26 00:03

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compagnie',
            fields=[
                ('compagnie_id', models.AutoField(primary_key=True, serialize=False)),
                ('nom_compagnie', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_equipement', models.CharField(max_length=50, unique=True)),
                ('quantite', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('code_IATTA', models.CharField(max_length=20)),
                ('nom_site', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'unique_together': {('site_id', 'code_IATTA')},
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('nom_terminal', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('nom_zone', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id_ticket', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('problem', 'Problem'), ('change', 'Change'), ('incident', 'Incident')], max_length=20)),
                ('type_intervention', models.CharField(choices=[('P', 'panne'), ('V', 'visite de maintenance'), ('AL', 'amenagement lourd'), ('I', 'installation'), ('D', 'drivers'), ('F', 'formation')], max_length=20)),
                ('nature_int', models.CharField(choices=[('P', 'preventif'), ('C', 'curatif'), ('M', 'modification'), ('TN', 'travaux neufs')], max_length=20)),
                ('type_communication', models.CharField(choices=[('T', 'telephone'), ('L', 'local')], max_length=20)),
                ('probleme', models.CharField(max_length=20, null=True)),
                ('solution', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('etat', models.CharField(choices=[('o', 'ouvert'), ('f', 'ferme'), ('a', 'annule')], max_length=20)),
                ('closed_at', models.DateTimeField(null=True)),
                ('compagnie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.compagnie')),
                ('equipement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.equipement')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.terminal')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.zone')),
            ],
        ),
        migrations.AddField(
            model_name='equipement',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site'),
        ),
        migrations.CreateModel(
            name='Comptoir',
            fields=[
                ('comptoir_Id', models.AutoField(primary_key=True, serialize=False)),
                ('comptoir_name', models.CharField(max_length=20)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site')),
            ],
        ),
        migrations.AddField(
            model_name='compagnie',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sita_app.site'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_administrateur', models.BooleanField(default=False)),
                ('is_help_desk', models.BooleanField(default=False)),
                ('is_consulteur', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='compagnie',
            unique_together={('nom_compagnie', 'site')},
        ),
    ]
