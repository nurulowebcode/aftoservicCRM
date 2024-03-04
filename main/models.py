from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File



class User(AbstractUser):
    full_name = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=13, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number',
        )])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self):
        return self.full_name



class Employee(models.Model):
    user_id = models.OneToOneField(to='User', on_delete=models.CASCADE)
    profession = models.CharField(max_length=200)
    wages = models.IntegerField()
    age = models.IntegerField(default=18)
    address = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    work_time = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=200)
    garage = models.ForeignKey(to='Garage', on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username



class Cassa(models.Model):
    summa = models.PositiveBigIntegerField(default=0)


class Order(models.Model):
    owner_name = models.CharField(max_length=200)
    owner_phone_number = models.CharField(max_length=13, unique=True)
    is_delivery = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    card_name = models.CharField(max_length=200)
    card_number = models.IntegerField()
    is_active = models.IntegerField(default=1, choices=(
        (1,'wait'),
        (2,'see'),
        (3,'saw'),
    ))
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    problem = models.CharField(max_length=255)
    service_cost = models.CharField(max_length=200)

    def __str__(self):
        return self.owner_name


class Payment(models.Model):
    order_id = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    code = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now=True,)
    admin = models.ForeignKey(to='Employee', on_delete=models.CASCADE)
    payment_type = models.IntegerField(default=3, choices=(
        (1,'card'),
        (2,'cash'),
        (3,'other'),
    ))
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order_id.owner_name}")
        qr.make(fit=True)
        img = qr.make_image(fill_coler="black", back_coler="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id.owner_name

class Garage(models.Model):
    number = models.IntegerField(default=0)



class Comment(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE)
    status = models.IntegerField(default=1, choices=(
        (1, 'comment'),
        (1, 'complain'),
        (1, 'sugestion'),
    ))
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)






