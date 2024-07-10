from django.db import models

# hello its me chandra

#hello this is supreme 

#hello lado khau aba pull gara

#timi muji chai lado khau aba push gara

class Category(models.Model):
   Name = models.CharField(max_length=50)
   #image = models.ImageField()
   def __str__(self):
        return self.Name
    

class Product(models.Model):
    Name = models.CharField(max_length= 50)
    Price = models.IntegerField(null= False)
    Description = models.CharField(max_length= 100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= "category", null = True)
    def __str__(self):
        return self.Name







