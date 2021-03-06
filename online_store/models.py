from django.db import models
from django.contrib.auth.models import AbstractUser
###On delete de oluyor bilmiyoruz!!!!!!!


class Account(AbstractUser):
    age       = models.IntegerField(null =True)
    sex       = models.BooleanField()


# https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/models/


class Customer(models.Model):
    cId       = models.AutoField(primary_key=True)
   # address   = models.CharField(max_length=500, null=True)
    taxNumber = models.IntegerField(null =True)  

    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name = "customer",
    )

class Address(models.Model):
    aId       = models.AutoField(primary_key=True,null = False)
    customer = models.ForeignKey('Customer', null = True,on_delete = models.SET_NULL,related_name="myAddress")
    address  = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s' % ( self.address)
    
class Images(models.Model):
    product = models.ForeignKey('Product', null = True,on_delete = models.SET_NULL,related_name="images")
    imgSrc  = models.CharField(max_length=200, null=True)

    def __str__(self):
        return '%s' % (self.imgSrc)

class ProductManager(models.Model):
    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = "productmanager",
    )
class SalesManager(models.Model):
    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name = "salesmanager",
    )

# Create your models here.
class Product(models.Model):
    ### Primary Key
    pId = models.AutoField(primary_key=True) 
    
    ### Table Specific Fields
    isActive         = models.NullBooleanField()

    price            = models.FloatField()
    oldPrice         = models.FloatField()
    stock            = models.IntegerField()  
    imgSrc           = models.CharField(max_length=100)
    name             = models.CharField(max_length=50) # TEXT 
    displayOldPrice  = models.BooleanField()
    cost             = models.FloatField()
    
    modelNo          = models.CharField(max_length=50) # TEXT ,BV200423 universal code
    description      = models.CharField(max_length=500) # TEXT
    warrantyStatus   = models.IntegerField()
    disturbuterInfo  = models.CharField(max_length=100) #TEXT
    categoryName     = models.ForeignKey('Category', null = True,on_delete = models.SET_NULL)
    listedDate       = models.DateField()

class Category(models.Model): # kategorinin son ??r??n?? silindi??inde kategori de silinsin mi???
    categoryName = models.CharField(max_length=80, primary_key=True)
    categoryIconScr = models.CharField(max_length=80)

# bir m????terinin birden fazla ??r??n almas??, sepetini g??rmesi,
# eski sipari??lerini g??r??nt??lemesi ??zellikleri
# en son bu class invoice de kullan??lacak ??r??n taraf?? olacak, ie bi
# her transactionda Client ve pIdleri s??yleyebilmeli
# ??rne??in g??n1 x ki??isi ??r??n 1 ve ??r??n 2 ald??. g??n2 x ki??isi bu sefere ??r??n3 ??r??n4 ?? ald??
# bize g??n1 de x ki??isinin ??r??n1 ve ??r??n 2 ald??????n?? s??ylebilmeli ayn?? ??ekilde ??r??n3 farkl?? 
# bir al????veri?? oldu??unu

class Basket(models.Model):
    bId            = models.AutoField(primary_key=True)
    cId            = models.ForeignKey('Customer', null = True,on_delete = models.SET_NULL)
    pId            = models.ForeignKey('Product', null = True,on_delete = models.SET_NULL) ##### de??i??tirsek 
    quantity       = models.IntegerField()
    totalPrice     = models.FloatField()
    purchasedDate  = models.DateField()
    isPurchased    = models.NullBooleanField()

    class Meta:
        unique_together = (('bId', 'cId'),)

 #   def Purchase():
  #      isPurchased =True
 #   def SeeMyBasket():
        # filter by isPurchased == False
 #   def SeeMyOldPurchases ():
        #filter by isPurchased == True
        #
        
#        Gok p1
#        Gok p2
#        gok p3
#        gok p4
        

class Delivery(models.Model):
    
    dId            = models.AutoField(primary_key=True)
    address        = models.CharField(max_length=500)
    IsDelivered    = models.NullBooleanField()

class Favourite(models.Model):
    fId            = models.AutoField(primary_key=True)
    cId            = models.ForeignKey('Customer', null=True,on_delete = models.SET_NULL)
    pId            = models.ForeignKey('Product', null = True,on_delete = models.SET_NULL) 
    class Meta:
        unique_together = (('fId', 'cId'),)


    #password  = forms.CharField(max_length=32, widget=forms.PasswordInput)


#add to basket
#    create new basket item with iscurrent set to true, if no entry with basket is current true.
#    else x
#*purchase 
#basketde isCurrent== True yoksa yeni basket objesi yarats??n
#ve sadece purchase ger??ekle??irse isCurrent = False

class Invoice(models.Model):
    price = models.FloatField(null = True)
    cost  = models.FloatField(null = True)
    iId = models.AutoField(primary_key=True)
    time  = models.DateTimeField(null=True)
    

    # we should inlcude date field
    # store profit and loss information 
    class Meta:
        unique_together = (('iId', 'bId','dId','cId'),)
    cId = models.ForeignKey('Customer', null=True,on_delete = models.SET_NULL)
    bId = models.ForeignKey('Basket', null = True,on_delete = models.SET_NULL) ##### de??i??tirsek 
    dId = models.ForeignKey('Delivery', null = True,on_delete = models.SET_NULL)

    oId = models.ForeignKey('Order', null = True,on_delete = models.SET_NULL)
    
class Order(models.Model):
    oId = models.AutoField(primary_key=True)

class Rating(models.Model):
    rId                 = models.AutoField(primary_key=True)
    pId                 = models.ForeignKey('Product', null=True,on_delete = models.SET_NULL,related_name ="productRating")
    cId                 = models.ForeignKey('Customer', null=True,on_delete = models.SET_NULL)
    rating              = models.IntegerField(null = True)
    commentbody         = models.CharField(max_length=200,null = True)
    commentHeader       = models.CharField(max_length=60,null = True)
    waitingForApproval  = models.NullBooleanField() # set True when a customer make a rating, set false when product manager
                                                    # makes a decision
    Approved            = models.NullBooleanField() # set True when product manager approves the rating
                                                    # false means comment is rejected
class Coupon(models.Model):
    couponId     = models.AutoField(primary_key=True)
    discountRate = models.FloatField(null = True)
    cId          = models.ForeignKey('Customer', null=True,on_delete = models.SET_NULL)
    couponName   = models.CharField(max_length=60,null = True)
    
#customer
#see my Ratings that wait for approval

#Product Manager
#see approvalList
#approve/reject Rating

#product
#see Rating
#add Rating
#delete Rating




#c1  #customer1 
#c1  #customer2 
#c2  #customer2 
#c2  #customer4 


#[c1:sport > c2:electronic > c3:pets > c4 > c5]


#c1 : ya???? 25 k??????klere sport g??ster 

#c1 #customer1 
#c1 #customer2 

