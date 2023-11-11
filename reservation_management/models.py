from django.db import models


class Client(models.Model):
    client_type = (
        ('b2b', 'B2B'),
        ('b2c', 'B2C'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=100, choices=client_type)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.email} - {self.phone}'

    client = models.Manager()

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return (f'{self.id} - {self.name} - {self.address} -'
                f'  {self.phone} - {self.city} - {self.country}')

    hotel = models.Manager()

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class HotelRoom(models.Model):
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.room_type} - {self.price} - {self.description}'

    hotel_room = models.Manager()

    class Meta:
        verbose_name = 'HotelRoom'
        verbose_name_plural = 'HotelRooms'


class Tour(models.Model):
    currency_choices = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('CLP', 'CLP'),
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, default=None)
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, null=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    initial_date = models.DateField(default=None)
    final_date = models.DateField(default=None)
    price = models.IntegerField(default=None)
    currency = models.CharField(max_length=10, choices=currency_choices)
    quantity = models.IntegerField(default=None)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return (f'{self.id} - {self.name} - {self.price} - {self.description} - '
                f'{self.initial_date} - {self.final_date} - {self.currency} - {self.total_price} '
                f'{self.client} - {self.hotel} - {self.hotel_room} - {self.quantity}')

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super(Tour, self).save(*args, **kwargs)

    tour = models.Manager()

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
