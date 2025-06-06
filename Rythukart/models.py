from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} ({self.number})"

    class Meta:
        db_table = 'rythukart_Register'  # Use your actual DB table name
        managed = False  # if here false nothing change here



class Product(models.Model):
        PRODUCT_TYPES = [
            ('veg', 'Vegetable'),
            ('pappu', 'Pappu'),
            ('rice', 'Rice'),
        ]

        name = models.CharField(max_length=100)
        product_type = models.CharField(max_length=10, choices=PRODUCT_TYPES)
        price = models.DecimalField(max_digits=10, decimal_places=2)  # New field
        image = models.ImageField(upload_to='products/')
        stock = models.PositiveIntegerField(default=0)  # <-- stock quantity

        @property
        def available(self):
            return self.stock > 0

        def __str__(self):
            return self.name
        class Meta:
            db_table = 'rythukart_Product'
            managed = False



        # models.py

class UserLocation(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pincode = models.CharField(max_length=10)
    address_line = models.CharField(max_length=100)
    near_by = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.near_by},{self.address_line},{self.area}, {self.district} ({self.pincode})"

    class Meta:
        db_table = 'rk_UserLocation'  # Use your actual DB table name
        managed = False  # if here false nothing change here



class Cart(models.Model):
    user = models.OneToOneField('Register', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.product.price * item.quantity for item in self.items.all())
    class Meta:
        db_table = 'rk_Cart'  # Use your actual DB table name
        managed = False  # if here false nothing change here

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product.price * self.quantity
    class Meta:
        db_table = 'rk_CartItem'  # Use your actual DB table name
        managed = False  # if here false nothing change here

# models.py

class Order(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField()
    status = models.CharField(max_length=50, default='Placed')  # Placed, Delivered, etc.
    class Meta:
        db_table = 'rythukart_order'  # Use your actual DB table name
        managed = False  # if here false nothing change here

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        db_table = 'rythukart_orderitem'  # Use your actual DB table name
        managed = False  # if here false nothing change here

class Invoice(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to='invoices/', blank=True, null=True)

    class Meta:
        db_table = 'rk_invoice'
