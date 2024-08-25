from django.db import models

class Book_table1(models.Model):
    Name = models.CharField(max_length=55)
    Email = models.EmailField(max_length=55)
    Number = models.IntegerField()
    Date = models.DateField()
    Person = models.IntegerField()
    def __str__(self):
        return str(self.Date)

class ItemList(models.Model):
    Category_Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Category_Name
    

class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Price=models.IntegerField()
    Category=models.ForeignKey(ItemList,related_name='Category_name',on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name

class Aboutus(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Ratings= models.IntegerField()
    Image=models.ImageField(upload_to='Items/')
    def __str__(self):
        return self.User_name
    


