# Generated by Django 4.0.4 on 2022-06-20 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companys', '0002_job_posting_jp_compensation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job_posting',
            options={'ordering': ['-id'], 'verbose_name': '채용공고', 'verbose_name_plural': '채용공고 목록'},
        ),
        migrations.AlterField(
            model_name='job_posting',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to='companys.company'),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companys.job_posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
