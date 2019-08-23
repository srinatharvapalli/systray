from django.db import models

class Customer_details(models.Model):
    IDNO = models.AutoField(primary_key=True)
    USERNAME = models.CharField(max_length=150)
    PASSWORD = models.CharField(max_length=150)
    EMAIL = models.EmailField(max_length=150)
    MOBILENO = models.CharField(max_length=10)
    OTP=models.CharField(max_length=50)


class Vendor_details(models.Model):
    IDNO = models.AutoField(primary_key=True)
    USERNAME = models.CharField(max_length=150)
    PASSWORD = models.CharField(max_length=150)
    EMAIL = models.EmailField(max_length=150)
    MOBILENO = models.CharField(max_length=10)
    OTP=models.CharField(max_length=50)

    def __str__(self):
        return self.USERNAME

class Add_newproduct(models.Model):
    V_P_ID = models.ForeignKey(Vendor_details, on_delete=models.CASCADE)
    VPID = models.AutoField(primary_key=True)
    TYPE = models.CharField(max_length=50)
    CATEGORIES = models.CharField(max_length= 50)
    CATEGORIETYPE = models.CharField(max_length= 50)
    SIZE = models.CharField(max_length=20)
    QUANTITY = models.CharField(max_length= 50)
    NAME = models.CharField(max_length= 100)
    IMAGE = models.ImageField(upload_to="my_images")
    PRICE = models.DecimalField(max_digits=10,decimal_places=2)
    DESCRIPTION = models.CharField(max_length=500)

class Vendor_Addresses(models.Model):
    V_A_ID = models.ForeignKey(Vendor_details,on_delete=models.CASCADE)
    VAID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=50)
    HOUSENUMBER = models.CharField(max_length=50)
    ADDRESS = models.CharField(max_length=150)
    CITY = models.CharField(max_length=50)
    STATE = models.CharField(max_length=50)
    PINCODE = models.CharField(max_length=10)
    LANDMARK = models.CharField(max_length=150)
    PHONE = models.CharField(max_length=10)

class Customer_Addcart(models.Model):
    C_ID = models.ForeignKey(Customer_details,on_delete=models.CASCADE)
    CAID = models.AutoField(primary_key=True)
    TYPE = models.CharField(max_length=50)
    CATEGORIES = models.CharField(max_length=50)
    CATEGORIETYPE = models.CharField(max_length=50)
    SIZE = models.CharField(max_length=20)
    QUANTITY = models.CharField(max_length=50)
    NAME = models.CharField(max_length=100)
    IMAGE = models.ImageField(upload_to="my_images")
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    DESCRIPTION = models.CharField(max_length=500)