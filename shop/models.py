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
    departament = models.ForeignKey(Departament, db_column='departament_id', on_delete=models.DO_NOTHING)
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
    display = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'product'
        managed = False


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, db_column='category_id', on_delete=models.DO_NOTHING)

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
    attribute = models.ForeignKey(Attribute, db_column='attribute_id', on_delete=models.DO_NOTHING)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = 'attribute_value'
        managed = False


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    attribute_value = models.ForeignKey(AttributeValue, db_column='attribute_value_id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'product_attribute'
        managed = False
        unique_together = (('product', 'attribute_value'),)


class ShoppingCart(models.Model):
    id = models.IntegerField(primary_key=True, db_column='item_id', editable=False)
    cart_id = models.CharField(max_length=32)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.BooleanField(default=True)
    added_on = models.DateField()

    class Meta:
        db_table = 'shopping_cart'
        managed = False


class ShippingRegion(models.Model):
    id = models.IntegerField(primary_key=True, db_column='shipping_region_id', editable=False)
    shipping_region = models.CharField(max_length=100)

    class Meta:
        db_table = 'shipping_region'
        managed = False


class Customer(models.Model):
    id = models.IntegerField(primary_key=True, db_column='customer_id', editable=False)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    credit_card = models.TextField()
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    shipping_region = models.ForeignKey(ShippingRegion, db_column='shipping_region_id', on_delete=models.DO_NOTHING)
    day_phone = models.CharField(max_length=100)
    eve_phone = models.CharField(max_length=100)
    mob_phone = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'
        managed = False


class Orders(models.Model):
    id = models.IntegerField(primary_key=True, db_column='order_id', editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    created_on = models.DateTimeField(auto_now_add=True)
    shipped_on = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)
    comments = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, db_column='customer_id', on_delete=models.DO_NOTHING)  # foreing key
    auth_code = models.CharField(max_length=50)
    reference = models.CharField(max_length=50)
    shipping = models.IntegerField()
    tax = models.IntegerField()

    class Meta:
        db_table = 'orders'
        managed = False


class OrderDetail(models.Model):
    id = models.IntegerField(primary_key=True, db_column='item_id', editable=False)
    order = models.ForeignKey(Orders, db_column='order_id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    attributes = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_detail'
        managed = False


class Shipping(models.Model):
    id = models.IntegerField(primary_key=True, db_column='shipping_id', editable=False)
    shipping_type = models.CharField(max_length=100)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_region = models.ForeignKey(ShippingRegion, db_column='shipping_region_id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'shipping'
        managed = False


class Tax(models.Model):
    id = models.IntegerField(primary_key=True, db_column='tax_id', editable=False)
    tax_type = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'tax'
        managed = False


class Audit(models.Model):
    id = models.IntegerField(primary_key=True, db_column='audit_id')
    order = models.ForeignKey(Orders, db_column='order_id', on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    code = models.IntegerField()

    class Meta:
        db_table = 'audit'
        managed = False


class Review(models.Model):
    id = models.IntegerField(primary_key=True, db_column='review_id', editable=False)
    customer = models.ForeignKey(Customer, db_column='customer_id', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.DO_NOTHING)
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'review'
        managed = False
