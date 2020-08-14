# Generated by Django 3.0.8 on 2020-08-13 11:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Категория')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_players', models.PositiveIntegerField(default=0)),
                ('number_of_players', models.PositiveIntegerField(default=0)),
                ('title', models.CharField(default='', max_length=32)),
                ('url', models.CharField(max_length=250, null=True)),
                ('file', models.FileField(default=None, null=True, upload_to='file/%Y/%m')),
                ('short_description', models.CharField(default='', max_length=250)),
                ('gameplay_video_link', models.CharField(default=None, max_length=250, null=True)),
                ('release_status', models.BooleanField(default=False)),
                ('date_release', models.DateField(default=datetime.date.today)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(default=None, null=True, upload_to='img/%Y/%m')),
                ('banner', models.ImageField(default=None, null=True, upload_to='img/%Y/%m')),
                ('description', models.TextField(default='')),
                ('genre', models.CharField(default='', max_length=50)),
                ('tags', models.CharField(default='', max_length=50)),
                ('rating', models.FloatField(default=0)),
                ('sale_percent', models.PositiveIntegerField(default=0)),
                ('is_hidden', models.BooleanField(default=False)),
                ('count_views', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='game_author', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(blank=True, related_name='categories', to='games.Category')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Жанр')),
                ('description', models.TextField(max_length=150, verbose_name='Описание')),
                ('img', models.ImageField(upload_to='genre', verbose_name='Иконка жанра')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Genre1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Жанр')),
                ('strategy', models.IntegerField(default=0)),
                ('rpg', models.IntegerField(default=0)),
                ('f2p', models.IntegerField(default=0)),
                ('shooter', models.IntegerField(default=0)),
                ('racing', models.IntegerField(default=0)),
                ('horror', models.IntegerField(default=0)),
                ('stealth', models.IntegerField(default=0)),
                ('survival_horror', models.IntegerField(default=0)),
                ('sports', models.IntegerField(default=0)),
                ('party', models.IntegerField(default=0)),
                ('platform', models.IntegerField(default=0)),
                ('puzzle', models.IntegerField(default=0)),
                ('god_game', models.IntegerField(default=0)),
                ('flight_simulation', models.IntegerField(default=0)),
                ('fighting', models.IntegerField(default=0)),
                ('beatemup', models.IntegerField(default=0)),
                ('adventure', models.IntegerField(default=0)),
                ('action', models.IntegerField(default=0)),
                ('simylate', models.IntegerField(default=0)),
                ('mmo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=None, null=True, upload_to='img/%Y/%m', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('question', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Views_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views_game', to='games.Game')),
            ],
            options={
                'verbose_name': 'Просмотр игры',
                'verbose_name_plural': 'Просмотры игр',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveIntegerField(default=0, null=True)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_author', to=settings.AUTH_USER_MODEL)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_game', to='games.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок записи')),
                ('text', models.TextField()),
                ('description', models.TextField(max_length=160, verbose_name='Короткое описание')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(null=True, upload_to='img/%Y/%m', verbose_name='Изображение записи')),
                ('num_views', models.PositiveIntegerField(default=0)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('fav', models.BooleanField(default=False, verbose_name='Избранное')),
                ('fav_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('image', models.ManyToManyField(blank=True, related_name='image', to='games.Media')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='games.Game')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ManyToManyField(blank=True, related_name='parent_game', to='games.Media'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='players', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='who_added_to_wishlist',
            field=models.ManyToManyField(blank=True, related_name='who_added_to_wishlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('moderation', models.BooleanField(default=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='games.Posts')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_post', to='games.Comments_Post', verbose_name='Родитель')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Comments_Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('moderation', models.BooleanField(default=True)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_game', to='games.Game')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_game', to='games.Comments_Game', verbose_name='Родитель')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='account', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_joined', models.DateField(default=datetime.date.today)),
                ('tel', models.CharField(max_length=12, null=True)),
                ('name', models.CharField(default='', max_length=30, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('date_birth', models.DateField(max_length=10, null=True, verbose_name='Дата рожения: ДД.ММ.ГГГГ')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='Город')),
                ('company', models.CharField(max_length=50, null=True, verbose_name='Компания')),
                ('bank_card', models.CharField(max_length=20, null=True, verbose_name='Номер карты')),
                ('is_player', models.BooleanField(default=False, null=True)),
                ('is_developer', models.BooleanField(default=False, null=True)),
                ('is_administrator', models.BooleanField(default=False, null=True)),
                ('bank_cаrd', models.CharField(max_length=20, null=True, verbose_name='Номер карты')),
                ('avatar', models.ImageField(null=True, upload_to='img/%Y/%m', verbose_name='Аватар')),
                ('fav_genres', models.ManyToManyField(blank=True, to='games.Genre')),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
            },
        ),
    ]
