from django.db import models
from decimal import Decimal

class Departament(models.Model):
    id = models.IntegerField(primary_key=True, db_column='departament_id', editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'departament'
        managed = False


class Category(models.Model):
    id = models.IntegerField(primary_key=True, db_column='category_id', editable=False)
    departament = models.ForeignKey(Departament, db_column='departament_id')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'category'
        managed = False


class Product(models.Model):
    id = models.IntegerField(primary_key=True, db_column='product_id', editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    image = models.CharField(max_length=150, null=True)
    image2 = models.CharField(max_length=150, null=True)
    thumbnail = models.CharField(max_length=150, null=True)
    discplay = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'product'
        managed = False


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, db_column='product_id')
    category = models.ForeignKey(Category, db_column='category_id')

    class Meta:
        db_table = 'product_category'
        managed = False
        unique_together = (('product', 'category'),)

class Attribute(models.Model):
    id = models.IntegerField(primary_key=True, db_column='attribute_id', editable=False)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'attribute'
        managed = False


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True, db_column='attribute_value_id', editable=False)
    attribute = models.ForeignKey(Attribute, db_column='attribute_id')
    value = models.CharField(max_length=100)

    class Meta:
        db_table = 'attribute_value'
        managed = False


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, db_column='product_id')
    attribute_value = models.ForeignKey(AttributeValue, db_column='attribute_value_id')

    class Meta:
        db_table = 'product_attribute'
        managed = False
        unique_together = (('product', 'attribute_value'),)


class ShoppingCart(models.Model):
    id = models.IntegerField(primary_key=True, db_column='item_id', editable=False)
    cart_id = models.CharField(max_length=32)
    product = models.ForeignKey(Product, db_column='product_id')
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.BooleanField(default=True)
    added_on = models.DateField()

    class Meta:
        db_table = 'shopping_cart'
        managed = False


class Orders(models.Model):
    id = models.IntegerField(primary_key=True, db_column='order_id', editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_on = models.DateTimeField(auto_now_add=True)
    shipped_on = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)
    comments = models.CharField(max_length=255)
    customer = models.IntegerField()
    auth_code = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    shipping = models.IntegerField()
    tax = models.IntegerField()

    class Meta:
        db_table = 'orders'
        managed = False


