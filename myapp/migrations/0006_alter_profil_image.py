# Generated by Django 4.1.4 on 2023-04-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_profil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='image',
            field=models.ImageField(auto_created='C:/Users/eldor/OneDrive/Documents/img/authors/rasm.8.jpg', upload_to='post/', verbose_name='profil rasmi'),
        ),
    ]
