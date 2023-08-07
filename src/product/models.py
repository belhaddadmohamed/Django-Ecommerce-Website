from django.db import models
from django.utils.translation import gettext_lazy as trans
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):
    prdName = models.CharField(max_length=100, verbose_name=trans("Product Name"))     # trans for translation 
    prdCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)    # 'category' to reference the model even if it is defined later 
    prdBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True)
    prdDesc = models.TextField(verbose_name=trans("Product Description"))
    prdImage = models.ImageField(upload_to="product/", blank=True, null=True)
    prdPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=trans("Price"))  # How much it will buy 
    prdPriceDiscount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=trans("Price Discount"))  # How much it will sale 
    prdCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=trans("Cost"))   # How much i purchase it
    prdCreated = models.DateTimeField(verbose_name=trans("Created At"))
    # Slug
    prdSlug = models.SlugField(blank=True, null=True)
    # Tags
    prdIsNew = models.BooleanField(default=True, verbose_name=trans("Product is New"))
    prdIsBestseller = models.BooleanField(default=False, verbose_name=trans("Product is Best Seller"))

    # Object Names 
    def __str__(self):
        return self.prdName
    
    # Create a slug when "Save" is clicked (Override method save())
    def save(self, *args, **kwargs):
        if not self.prdSlug:
            self.prdSlug = slugify(self.prdName)
        super(Product, self).save(*args, **kwargs)

    # Get the url of the product (Instead of using {% url .... %})
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.prdSlug})
        
    # Class names  
    class Meta:
        verbose_name = trans("Product")
        verbose_name_plural = trans("Products")
    


class ProductImage(models.Model):
    proProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    proIMage = models.ImageField(upload_to="product/")

    # Object Names 
    def __str__(self):
        return str(self.proProduct)
    
    # Class names  
    class Meta:
        verbose_name = trans("Product image")
        verbose_name_plural = trans("Product images")
        


class Category(models.Model):
    catName = models.CharField(max_length=80, verbose_name=trans("Category Name"))
    catParent = models.ForeignKey('self', on_delete=models.CASCADE, 
                                  limit_choices_to={'catParent__isnull' : True},
                                  verbose_name=trans("Main Category"),
                                  blank=True, null=True)
    catDesc = models.TextField(verbose_name=trans("Description"))
    catImg = models.ImageField(upload_to='category/', verbose_name=trans("Image"))

    # Object Names 
    def __str__(self):
        return self.catName
    
    # Class names  
    class Meta:
        verbose_name = trans("Category")
        verbose_name_plural = trans("Categories")



class ProductAlternatives(models.Model):
    altProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=trans("Product"), related_name="main_Product")
    altAlternatives = models.ManyToManyField(Product, verbose_name=trans("Alternatives"), related_name="Product_Alternatives")

    def __str__(self):
        return str(self.altProduct)

    class Meta:
        verbose_name = trans("Alternative")
        verbose_name_plural = trans("Alternatives")



class ProductAccessories(models.Model):
    accProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=trans("Product"), related_name="main_product")
    accAccessories = models.ManyToManyField(Product, verbose_name=trans("Accessories"), related_name="Product_accessories")

    def __str__(self):
        return str(self.accProduct)
    
    class Meta:
        verbose_name = trans("Product Accessory")
        verbose_name_plural = trans("Product Accessories")