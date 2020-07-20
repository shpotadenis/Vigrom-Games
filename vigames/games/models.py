from django.db import models
from datetime import date

class Category(models.Model):
    # Модель категорий
    name = models.CharField("Категория", max_length=100)
    descriptions= models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Registration(models.Model):
    # Регистрация пользователя
    login = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    date_reg = models.DateField(date.today)

    def __str__(self):
        return self.login

class Account():
    # Аккаунт пользователя
    user = models.OneToOneField(Registration, on_delete=models.CASCADE, primary_key=True)   # Достаем из базы данные регистрации
    tel = models.CharField(max_length=12)   # Номер телефона
    '''Пока номер телефона вводится просто как строка без проверки. В будущем можно будет заменить на этот код:
    from django.core.validators import RegexValidator
    class PhoneModel(models.Model):
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
        phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    '''
    name = models.CharField("Имя", max_length=30)
    lastname = models.CharField("Фамилия", max_length=30)
    date_birth = models.CharField("Дата рожения: ДД.ММ.ГГГГ", max_length=10)
    city = models.CharField("Город", max_length=50, null=True)
    company = models.CharField("Компания", max_length=50)
    bank_card = models.CharField("Номер карты", max_length=20)
    #Добавить список игр - скорее всего связь многие ко многим

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

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

class Role(models.Model):
    #Роль на сайте. В базе прописываются 3 позиции Пользователь/разработчик/модератор.
    #При регистрации выбор между двумя Пользователь/разрабочик
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    role = models.CharField("Пользователь/разработчик", max_length=50)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

class Posts(models.Model):
    # Модель записи в блоге
    author = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField("Заголовок записи", max_length=150)
    url = models.SlugField(max_length=100, unique=True)
    text = models.TextField()
    description = models.TextField("Короткое описание", max_length=160)
    data = models.DateField(date.today)
    # Вопрос по изображениям открыт. Делать для них отдельную модель или сделать загрузку сюда???
    # Вопрос с количеством просмотров тоже открыт

class Game(models.Model):
    # Модель игры
    pass

class comment(models.Model):
    # Комментарий
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    text_comment = models.TextField()

    def __str__(self):
        return self.text_comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

