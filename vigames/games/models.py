from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User


class Media(models.Model):
    title = models.CharField('Заголовок изображения', max_length=50)
    img = models.ImageField("Изображение", upload_to="img/%Y/%m")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class Genre(models.Model):
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


class Account(models.Model):
    # Аккаунт пользователя
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
    #strategy = models.IntegerField(default=0)
    #rpg = models.IntegerField(default=0)
    #f2p = models.IntegerField(default=0)
    #shooter = models.IntegerField(default=0)
    #racing = models.IntegerField(default=0)
    #horror = models.IntegerField(default=0)
    #stealth = models.IntegerField(default=0)
    #survival_horror = models.IntegerField(default=0)
    #sports = models.IntegerField(default=0)
    #party = models.IntegerField(default=0)
    #platform = models.IntegerField(default=0)
    #puzzle = models.IntegerField(default=0)
    #god_game = models.IntegerField(default=0)
    #flight_simulation = models.IntegerField(default=0)
    #fighting = models.IntegerField(default=0)
    #beatemup = models.IntegerField(default=0)
    #adventure = models.IntegerField(default=0)
    #action = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class Category(models.Model):
    # Модель категорий
    name = models.CharField("Категория", max_length=100)
    descriptions = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

#в продакшене выпилить некоторые null=True (сейчас удобно тестировать с ними)
class Game(models.Model):
    players = models.ManyToManyField(Account, blank=True, related_name="players")
    who_added_to_wishlist = models.ManyToManyField(Account, blank=True, related_name="who_added_to_wishlist")
    author = models.ForeignKey(Account, on_delete=models.PROTECT,
                                        related_name="game_author", null=True)
    categories = models.ManyToManyField(Category, blank=True, related_name="categories")
    title = models.CharField(max_length=32, default="")
    #url = models.CharField(max_length=250, null=True)  # по идее можно выпилить?
    file = models.FileField(null=True, upload_to=u'file/%Y/%m', default=None)
    short_description = models.CharField(max_length=250, default="")
    image = models.ImageField('Изображение игры', upload_to='img/%Y/%m', null=True, default=None)
    gameplay_video_link = models.CharField(max_length=250, null=True, default=None)
    release_status = models.BooleanField(default=False)
    date_release = models.DateField(default=date.today)
    price = models.IntegerField(default=0)
    screenshots = models.ImageField(upload_to='img/%Y/%m', null=True, default=None)
    # uploads
    description = models.TextField(default="")
    genre = models.CharField(max_length=50, default="")
    tags = models.CharField(max_length=50, default="")
    rating = models.FloatField(default=0)
    sale_percent = models.PositiveIntegerField(default=0)

    

'''
class Basket(models.Model):
    # Корзина
    #account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    # ДОбавить список игр в корзине - связь многие ко многим
    #Корзину вероятно придется хранить не в базе данных, а в куки
'''


class Orders(models.Model):
    # Заказы
    pass


class Posts(models.Model):
    # Модель записи в блоге
    # author = models.ManyToManyField(User, default='admin')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    liked = models.ManyToManyField(Account, blank=True, related_name="liked")
    disliked = models.ManyToManyField(Account, blank=True, related_name="disliked")

    #в принципе можно убрать счетчики и искать кол-во лайкнувших/дизлайкнувших людей,
    #посмотреть, как удобнее
    count_likes = models.PositiveIntegerField(default=0)
    count_dislikes = models.PositiveIntegerField(default=0)

    title = models.CharField("Заголовок записи", max_length=150)
    url = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    description = models.TextField("Короткое описание", max_length=160)
    data = models.DateTimeField(auto_now_add=True)
    img = models.ImageField('Изображение записи', upload_to='img/%Y/%m', null=True)    # Главная фотография записи
    num_views = models.PositiveIntegerField(default=0)  # Хранит количество просмотров записи
    draft = models.BooleanField("Черновик", default=False)
    forthegame = models.IntegerField(default=0)

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
    # Комментарий к игре
    page = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text_comment = models.TextField()
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Comments_Post(models.Model):
    # Комментарий к записи
    page = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text_comment = models.TextField()
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_author", null=True)
    mark = models.PositiveIntegerField(default=0, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                                    related_name="game", null=True)

