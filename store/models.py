from django.db import models

# Create your models here.

class ProductCategory(models.Model):
	name = models.CharField(max_length=200, unique=True)
	description = models.TextField(max_length=400)
	class Meta:
		verbose_name = 'Categoria de Producto'
		verbose_name_plural = 'Categorias de productos'
	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=255, null=False, unique=True)
	price = models.IntegerField(null=False)
	description = models.TextField(max_length=400)
	image_url = models.TextField(max_length=600)
	category = models.ForeignKey(ProductCategory)
	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'
	def __str__(self):
		return self.name

class Customer(models.Model):
	messenger_user_id = models.CharField(max_length=30, unique=True)
	name = models.CharField(max_length=200, blank=True)
	phone = models.CharField(max_length=10)
	email = models.EmailField(help_text="Email address")
	class Meta:
        	verbose_name = 'Cliente'
        	verbose_name_plural = 'Clientes'
	def __str__(self):
		return str(self.name)

class Order(models.Model):
	TYPES = (
		('NEW','New Order'),
		('ONC','Order On Course'),
		('DEL','Order Deleted'),
		('FIN','Order Finished'),
		('CLD','Order Closed'),
	)
	PAYMENT = (
		('CASH','Dinero en efectivo'),
		('TERM','Datafono'),
	)
	state = models.CharField(max_length=3, choices= TYPES,default='NEW')
	customer = models.CharField(max_length=30, default="0")
	date = models.DateTimeField()
	payment_method = models.CharField(max_length=4, choices=PAYMENT, default="CASH")
	delivery_address = models.TextField(max_length=600)
	subtotal = models.IntegerField()
	shipping_cost = models.IntegerField()
	total_tax = models.IntegerField()
	total_cost = models.IntegerField()
	class Meta:
        	verbose_name = 'Orden'
        	verbose_name_plural = 'Ordenes'
    	def __str__(self):
        	#return str(self.pk)
		return u'Order ID: %s -  State: %s'%(self.pk,self.state)

class OrderItems(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	class Meta:
        	verbose_name = 'Item de Orden'
        	verbose_name_plural = 'Items de ordenes'
    	def __str__(self):
        	return u'Order ID: %s - Product: %s'%(self.order.pk,self.product.name)
