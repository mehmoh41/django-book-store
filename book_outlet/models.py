from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.urls import reverse


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}, {self.code}"
    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    # inner classes are used for meta configuration
    class Meta:
        verbose_name_plural = "Address Entries"
        

class Author(models.Model): 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address , on_delete= models.CASCADE , null=True)
    # foreignkey is used for many to one relations

    def full_name(self):
        return f"{self.first_name} {self.last_name}" 

    def __str__(self):
        return self.full_name()

class Book(models.Model) :
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE , null=True,related_name="books")
    published_counteries = models.ManyToManyField(Country,related_name="countries")
    # CASCADE means if a author deleted any related books should also be deleted
    # SETNULL ...
    is_best_selling_book = models.BooleanField(default=False)
    slug = models.SlugField(default="" , blank=True, null=False , db_index=True)

    def get_absolute_url(self):
        # kwargs={"pk": self.pk}
        return reverse("book-detail", args=[self.slug] )
    
    # def save(self , *args , **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save( *args , **kwargs)
    
    def __str__(self):
        return f"{self.title} ({self.rating}) ({self.is_best_selling_book}) author: ({self.author}) slug: ({self.slug})"