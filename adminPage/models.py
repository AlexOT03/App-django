from django.db import models

# Create your models here.
class Places(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Orders(models.Model):
    date = models.DateField()
    places = models.ForeignKey(Places, on_delete=models.CASCADE)
    description = models.TextField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"orders {self.id} - {self.places.name}"

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    affair = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"Mensaje de {self.name} - {self.affair}"