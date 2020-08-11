from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class Genre(models.Model):
    """Модель жанров игр"""

    name = models.CharField('Жанр', max_length=20, unique=True)
    description = models.TextField('Описание', max_length=150)
    img = models.ImageField("Иконка жанра", upload_to="genre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    """
    strategy = models.IntegerField(default=0)
    rpg = models.IntegerField(default=0)
    f2p = models.IntegerField(default=0)
    shooter = models.IntegerField(default=0)
    racing = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival_horror = models.IntegerField(default=0)
    sports = models.IntegerField(default=0)
    party = models.IntegerField(default=0)
    platform = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)
    god_game = models.IntegerField(default=0)
    flight_simulation = models.IntegerField(default=0)
    fighting = models.IntegerField(default=0)
    beatemup = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    simylate = models.IntegerField(default=0)
    mmo = models.IntegerField(default=0)
    """


class Genre1(models.Model):
    name = models.CharField('Жанр', max_length=20, unique=True)
    strategy = models.IntegerField(default=0)
    rpg = models.IntegerField(default=0)
    f2p = models.IntegerField(default=0)
    shooter = models.IntegerField(default=0)
    racing = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival_horror = models.IntegerField(default=0)
    sports = models.IntegerField(default=0)
    party = models.IntegerField(default=0)
    platform = models.IntegerField(default=0)
    puzzle = models.IntegerField(default=0)
    god_game = models.IntegerField(default=0)
    flight_simulation = models.IntegerField(default=0)
    fighting = models.IntegerField(default=0)
    beatemup = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    action = models.IntegerField(default=0)
    simylate = models.IntegerField(default=0)
    mmo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class Account(models.Model):
    """Модель аккаунтов пользователей"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)  # Достаем из базы
    # данные регистрации
    fav_genres = models.ManyToManyField(Genre, blank=True)
    date_joined = models.DateField(default=date.today)
    tel = models.CharField(max_length=12, null=True)  # Номер телефона
    '''Пока номер телефона вводится просто как строка без проверки. В будущем можно будет заменить на этот код:
    from django.core.validators import RegexValidator
    class PhoneModel(models.Model):
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    '''
    name = models.CharField("Имя", max_length=30, null=True, default="")
    lastname = models.CharField("Фамилия", max_length=30, null=True)
    date_birth = models.DateField("Дата рожения: ДД.ММ.ГГГГ", max_length=10, null=True)
    city = models.CharField("Город", max_length=50, null=True)
    company = models.CharField("Компания", max_length=50, null=True)
    bank_card = models.CharField("Номер карты", max_length=20, null=True)
    is_player = models.BooleanField(default=False, null=True)
    is_developer = models.BooleanField(default=False, null=True)
    is_administrator = models.BooleanField(default=False, null=True)
    bank_cаrd = models.CharField("Номер карты", max_length=20, null=True)
    foto = models.ImageField("Аватар", upload_to="img/%Y/%m", null=True)

    # strategy = models.IntegerField(default=0)
    # simylate = models.IntegerField(default=0)
    # mmo = models.IntegerField(default=0)
    # shooter = models.IntegerField(default=0)
    # adventure = models.IntegerField(default=0)
    # horror = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class Category(models.Model):
    """Модель категорий"""

    name = models.CharField("Категория", max_length=100, unique=True)
    descriptions = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Media(models.Model):
    """Модель изображений"""

    # title = models.CharField('Заголовок изображения', max_length=50)
    img = models.ImageField("Изображение", upload_to="img/%Y/%m", null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    '''
    def __str__(self):
        return self.img
    '''

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


# в продакшене выпилить некоторые null=True (сейчас удобно тестировать с ними)
class Game(models.Model):
    """Модель игр"""

    players = models.ManyToManyField(User, blank=True, related_name="players")
    number_of_players = models.PositiveIntegerField(default=0)
    who_added_to_wishlist = models.ManyToManyField(User, blank=True, related_name="who_added_to_wishlist")
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name="game_author", null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="categories")
    title = models.CharField(max_length=32, default="")
    url = models.CharField(max_length=250, null=True)  # по идее можно выпилить?
    file = models.FileField(null=True, upload_to=u'file/%Y/%m', default=None)
    short_description = models.CharField(max_length=250, default="")
    # image = models.ImageField('Изображение игры', upload_to='img/%Y/%m', null=True, default=None)
    gameplay_video_link = models.CharField(max_length=250, null=True, default=None)
    release_status = models.BooleanField(default=False)
    date_release = models.DateField(default=date.today)
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='img/%Y/%m', null=True, default=None)
    banner = models.ImageField(upload_to='img/%Y/%m', null=True, default=None)
    # uploads
    description = models.TextField(default="")
    #genre = models.ManyToManyField(Genre, blank=True, related_name='genre', null=True)
    genre = models.CharField(max_length=50, default="")
    tags = models.CharField(max_length=50, default="")
    rating = models.FloatField(default=0)
    sale_percent = models.PositiveIntegerField(default=0)
    image = models.ManyToManyField(Media, blank=True, related_name='parent_game')
    #num_views = models.PositiveIntegerField(default=0)  # Хранит количество просмотров игры
    is_hidden = models.BooleanField(default=False)
    '''
    screenshots1 = models.ImageField(upload_to='img/%Y/%m', null=True)
    screenshots2 = models.ImageField(upload_to='img/%Y/%m', null=True)
    screenshots3 = models.ImageField(upload_to='img/%Y/%m', null=True)
    screenshots4 = models.ImageField(upload_to='img/%Y/%m', null=True)
    '''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class Views_Game(models.Model):
    """ Модель просмотров игры """
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='views_game')
    num = models.PositiveIntegerField(default=0)  # Хранит количество просмотров игры
    date = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Просмотр игры"
        verbose_name_plural = "Просмотры игр"
'''
class Basket(models.Model):
    # Корзина
    #account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    # ДОбавить список игр в корзине - связь многие ко многим
    #Корзину вероятно придется хранить не в базе данных, а в куки
'''


class Orders(models.Model):
    """Модель заказов (покупки) игр"""

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    game = models.ForeignKey(Game, null=True, on_delete=models.SET_NULL, related_name='orders')
    price = models.IntegerField(null=True)
    date = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Posts(models.Model):
    """Модель записей в блоге (новости)"""

    # author = models.ManyToManyField(User, default='admin')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #liked = models.ManyToManyField(Account, blank=True, related_name="liked")
    #disliked = models.ManyToManyField(Account, blank=True, related_name="disliked")

    # в принципе можно убрать счетчики и искать кол-во лайкнувших/дизлайкнувших людей,
    # посмотреть, как удобнее
    #count_likes = models.PositiveIntegerField(default=0)
    #count_dislikes = models.PositiveIntegerField(default=0)

    title = models.CharField("Заголовок записи", max_length=150)
    # url = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    description = models.TextField("Короткое описание", max_length=160)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField('Изображение записи', upload_to='img/%Y/%m', null=True)  # Главная фотография записи
    num_views = models.PositiveIntegerField(default=0)  # Хранит количество просмотров записи
    draft = models.BooleanField("Черновик", default=False)
    image = models.ManyToManyField(Media, blank=True, related_name='image')
    fav = models.BooleanField('Избранное', default=False)
    fav_date = models.DateTimeField(auto_now=True, blank=True) #было auto_now_add=True, ругался
    # Вопрос по изображениям открыт. Делать для них отдельную модель или сделать загрузку сюда???
    # Вопрос с количеством просмотров тоже открыт

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post-url', args=[str(self.url)])

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comments_Game(models.Model):
    """Модель комментариев к играм"""

    page = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments_game', null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text_comment = models.TextField()
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children_game')
    date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Comments_Post(models.Model):
    """Модель комментариев к новостям"""

    page = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments_post', null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text_comment = models.TextField()
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children_post')
    date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Review(models.Model):
    """Модель отзывов к играм"""

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_author", null=True)
    mark = models.PositiveIntegerField(default=0, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews_game", null=True)
    title = models.CharField(null=True, max_length=70, blank=True)
    comment = models.CharField(null=True, max_length=500, blank=True)


class FAQ(models.Model):
    """Модель вопросов и ответов в Faq"""

    question = models.CharField(max_length=150)
    answer = models.TextField()


class Question(models.Model):
    """Модель вопросов к администраторам сайта"""

    email = models.EmailField()
    question = models.CharField(max_length=500)
