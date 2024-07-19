from django.db import models

class Banner(models.Model):
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    background = models.ImageField(upload_to='background/', blank=True, null=True)
    title = models.CharField(max_length=55)
    about = models.TextField()

    def __str__(self) -> str:
        return f"{self.title}"
    
    
class AboutAs(models.Model):
    image = models.ImageField(upload_to='aboutas/')
    title = models.CharField(max_length=55)
    text = models.TextField()
    network_url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    
class Contact(models.Model):
       lacation = models.CharField(max_length=320)
       contact_center = models.CharField(max_length=13)
       email = models.EmailField()

       def __str__(self) -> str:
           return self.email
       
       
class WorkingTime(models.Model):
    text = models.TextField()

    def __str__(self) -> str:
        return self.id
    
class Message(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.CharField(max_length=32)
    question = models.TextField()

    def __str__(self) -> str:
        return self.subject
    
class Feadback(models.Model):
    image = models.ImageField(upload_to='feadback-user/')
    name = models.CharField(max_length=55)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name
    

class ProductsMenu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-image/')
    name = models.CharField(max_length=55)
    about = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name} - {self.category} - {self.id}"

    
class DiscountProduct(models.Model):
    product = models.ManyToManyField(ProductsMenu, related_name='product')
    percent = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.percent} - {self.product.name}"

    
