from django.conf import settings
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    kitchen = models.CharField(max_length=50, verbose_name="Кухня")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    description = models.TextField(blank=True, verbose_name="Описание")
    average_check = models.PositiveIntegerField(default=1000, verbose_name="Средний чек")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, verbose_name="Рейтинг")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Dish(models.Model):
    class Category(models.TextChoices):
        SALAD = "salad", "Салаты"
        SOUP = "soup", "Супы"
        HOT = "hot", "Горячее"
        MEAT = "meat", "Мясные Блюда"
        SNACKS = "snacks", "Закуски"
        DESSERT = "dessert", "Десерты"
        DRINK = "drink", "Напитки"
        SIDE = "side", "Гарниры"
        KHINKALI = "khinkali", "Хинкали"
        KHACHAPURI = "khachapuri", "Хачапури"

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="dishes",
        verbose_name="Ресторан",
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.HOT,
        verbose_name="Категория",
    )
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    is_available = models.BooleanField(default=True, verbose_name="Доступно")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"


class Booking(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "Новая"
        CONFIRMED = "confirmed", "Подтверждена"
        CANCELLED = "cancelled", "Отменена"
        COMPLETED = "completed", "Завершена"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Пользователь",
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Ресторан",
    )
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    guests = models.PositiveSmallIntegerField(default=2, verbose_name="Гостей")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Статус",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.restaurant.name} — {self.date} {self.time}"