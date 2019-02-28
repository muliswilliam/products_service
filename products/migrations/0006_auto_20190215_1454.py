# Generated by Django 2.0.7 on 2019-02-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190214_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(blank=True, help_text='Distinguishing look or color of  product', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='workflowlevel2_uuid',
            field=models.CharField(blank=True, help_text='Unique ID to relate back  to Bifrost workflow', max_length=255, verbose_name='WorkflowLevel2 UUID'),
        ),
    ]