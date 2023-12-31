from django.db import models


class Client(models.Model):
    client_type = (
        ('b2b', 'B2B'),
        ('b2c', 'B2C'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=client_type)

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
    country = models.CharField(max_length=20)

    def __str__(self):
        return (f'{self.id} - {self.name} - {self.address} -'
                f'  {self.phone} - {self.city} - {self.country}')

    hotel = models.Manager()

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class HotelRoom(models.Model):
    room_type_choices = (
        ('individual', 'Individual'), ('doble', 'Doble'),
        ('triple', 'Triple'), ('quad', 'Quad'), ('queen', 'Queen'),
        ('king', 'King')
    )
    room_type = models.CharField(max_length=20, choices=room_type_choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.id} - {self.room_type} - {self.price} - {self.description}'

    hotel_room = models.Manager()

    class Meta:
        verbose_name = 'HotelRoom'
        verbose_name_plural = 'HotelRooms'


class Tour(models.Model):
    currency_choices = (
        ('USD', 'USD'), ('EUR', 'EUR'), ('CLP', 'CLP')
    )
    mobilization_choices = (
        ('auto', 'Auto'), ('van', 'Van'), ('bus', 'Bus')
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, default=None)
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, null=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, default=None)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    initial_date = models.DateField(default=None)
    final_date = models.DateField(default=None)
    price = models.IntegerField(default=None)
    currency = models.CharField(max_length=10, choices=currency_choices)
    quantity = models.IntegerField(default=0)
    sub_total = models.IntegerField(default=0)
    mobilization = models.CharField(max_length=10, choices=mobilization_choices, default=None)
    discount = models.IntegerField(default=0)
    iva_application = models.BooleanField(default=False)
    iva = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def __str__(self):
        return (f'{self.id} - {self.name} - {self.price} - {self.description} - {self.iva_application}'
                f'{self.initial_date} - {self.final_date} - {self.currency} - {self.sub_total} '
                f'{self.client} - {self.hotel} - {self.hotel_room} - {self.quantity} - {self.mobilization} - '
                f'{self.discount}')

    def save(self, *args, **kwargs):
        original_sub_total = self.price * self.quantity

        if not self.iva_application and self.discount == 0:
            self.iva = 0
            self.sub_total = original_sub_total
            self.total = self.sub_total
        elif self.iva_application and self.discount != 0:
            self.discount = (self.discount * original_sub_total) / 100
            self.sub_total = original_sub_total - self.discount
            self.iva = self.sub_total * 0.19
            self.total = self.sub_total + self.iva

        super(Tour, self).save(*args, **kwargs)

    tour = models.Manager()

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'


class Day(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, null=True, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.client} - {self.tour}'

    day = models.Manager()

    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Days'


