# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 06:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0001_initial'),
        ('level', '0001_initial'),
        ('configsettings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True)),
                ('wechat', models.CharField(blank=True, max_length=255, null=True)),
                ('qq', models.CharField(blank=True, max_length=255, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Rejected'), (1, 'Active'), (2, 'Inactive'), (3, 'Pending')], default=1, null=True)),
                ('promo_code', models.CharField(blank=True, max_length=255, null=True)),
                ('referring_url', models.CharField(blank=True, max_length=255, null=True)),
                ('initiated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_banking_info', to='bank.BankInfo')),
                ('commission_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_commission_settings', to='configsettings.CommissionSettings')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_created_by', to=settings.AUTH_USER_MODEL)),
                ('default_member_lv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_default_level', to='level.Level')),
                ('default_return_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_default_return_settings', to='configsettings.ReturnSettings')),
            ],
            options={
                'db_table': 'account_agent',
            },
        ),
        migrations.CreateModel(
            name='AgentLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'account_level',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('wechat', models.CharField(blank=True, max_length=255, null=True)),
                ('qq', models.CharField(blank=True, max_length=255, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Rejected'), (1, 'Active'), (2, 'Inactive'), (3, 'Pending')], default=1, null=True)),
                ('level_lock', models.IntegerField(choices=[(0, 'Locked'), (1, 'Unlocked')], default=1)),
                ('referring_url', models.CharField(blank=True, max_length=255, null=True)),
                ('initiated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_agent', to='account.Agent')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_banking_info', to='bank.BankInfo')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_created_by', to=settings.AUTH_USER_MODEL)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_level', to='level.Level')),
                ('return_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_return_settings', to='configsettings.ReturnSettings')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_member',
            },
        ),
        migrations.AddField(
            model_name='agent',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent_level', to='account.AgentLevel'),
        ),
        migrations.AddField(
            model_name='agent',
            name='parent_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='account.Agent'),
        ),
        migrations.AddField(
            model_name='agent',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agent_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
