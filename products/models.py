from django.db import models

from cores.models import TimeStamp

class Main(models.Model) :
    name              = models.CharField(max_length=50)

    class Meta :
        db_table = 'mains'


class Category(models.Model) :
    name              = models.CharField(max_length=100)
    main              = models.ForeignKey('Main', on_delete=models.CASCADE)

    class Meta :
        db_table = 'categories'


class Product(TimeStamp) :
    category          = models.ForeignKey('Category', on_delete=models.CASCADE)
    name              = models.CharField(max_length=100)
    usage             = models.CharField(max_length=100)
    texture           = models.CharField(max_length=100)
    direction         = models.CharField(max_length=100)
    detail            = models.CharField(max_length=1000)
    is_new            = models.BooleanField(default=False)
    skin              = models.ManyToManyField('Skin', through="Product_Skin")
    scent             = models.ManyToManyField('Scent', through="Product_Scent")

    class Meta :
        db_table = 'products'


class ProductSkin(models.Model) : 
    product           = models.ForeignKey('Product', on_delete=models.CASCADE)
    skin              = models.ForeignKey('Skin', on_delete=models.CASCADE)

    class Meta :
        db_table = 'productskins'


class Skin(models.Model) :
    skin_type         = models.CharField(max_length=30)

    class Meta :
        db_table = 'skins'


class ProductScent(models.Model) : 
    product           = models.ForeignKey('Product', on_delete=models.CASCADE)
    scent             = models.ForeignKey('Scent', on_delete=models.CASCADE)

    class Meta :
        db_table = 'productscents'


class Scent(models.Model) :
    scent_name        = models.CharField(max_length=30)

    class Meta :
        db_table = 'scents'


class Image(models.Model) :
    product_id        = models.ForeignKey('Product', on_delete=models.CASCADE)
    image_url         = models.CharField(max_length=200)

    class Meta :
        db_table = 'images'


class Selection(models.Model) :
    product_id        = models.ForeignKey('Product', on_delete=models.CASCADE)
    size              = models.IntegerField()
    price             = models.DecimalField(max_digits = 7, decimal_places = 2)

    class Meta :
        db_table = 'selections'


class Ingredient(models.Model) :
    product_id        = models.ForeignKey('Product', on_delete=models.CASCADE)
    ingredient_name   = models.CharField(max_length=50)
    detail_text       = models.CharField(max_length=500)

    class Meta :
        db_table = 'ingredients'