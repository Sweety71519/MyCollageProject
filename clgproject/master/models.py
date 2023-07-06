from django.db import models

# Create your models here.

from django.db import models


from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import AbstractUser

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']



class Product(models.Model):
    pid=models.IntegerField(primary_key=True,default=1)
    product_name=models.CharField(max_length=250)
    product_code=models.CharField(max_length=50)
    created_on=models.DateField(auto_now=True)


class ProductData(models.Model):
    id = models.IntegerField(blank=True)
    productcode=models.BigAutoField(primary_key=True)
    productname=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=250)
    status=models.BooleanField(default=True)
    created_on=models.DateField(auto_now=True)
    updated_at=models.DateField()



class Country(models.Model):
    countrycode = models.IntegerField(blank=True)
    countryname = models.CharField(max_length=50, blank=True)
    isdcode = models.IntegerField(blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        ordering = ['countryname']


class Zone(models.Model):
    id = models.BigAutoField(primary_key=True)
    zonecode = models.IntegerField(blank=False,default=1)
    zonename = models.CharField(max_length=20, blank=True)
    countrycode=models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['zonename']


class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    countrycode=models.ForeignKey(Country, on_delete=models.CASCADE)
    statecode=models.IntegerField(blank=False,default=1)
    zonecode = models.IntegerField(blank=True)
    statename = models.CharField(max_length=50, blank=True)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['statename']



class Areamaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    statecode=models.IntegerField(blank=False)
    zonecode = models.IntegerField(blank=False,)
    countrycode=models.IntegerField(blank=False)
    areacode=models.IntegerField(blank=False,)
    areaname = models.CharField(max_length=50, blank=True)
    status=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['areaname']

class Area(models.Model):
    countrycode = models.ForeignKey(Country, on_delete=models.CASCADE)
    statecode = models.ForeignKey(State, on_delete=models.CASCADE)
    #countrycode=models.IntegerField(blank=False)
    # statecode=models.IntegerField(blank=False)
    areacode = models.BigAutoField(primary_key=True)
    areaname= models.CharField(max_length=50, blank=False)
    status=models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    class Meta:
        ordering = ['areaname']
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.id == None:
            self.id = self.areacode
            super().save()


class District(models.Model):
    id = models.IntegerField(blank=True)
    districtcode = models.BigAutoField(primary_key=True)
    statecode=models.IntegerField(blank=False)
    districtname=models.CharField(max_length=50, blank=True)
    countrycode=models.IntegerField(blank=False)
    areacode=models.IntegerField(blank=False)
    status =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['districtname']


class City(models.Model):
    id = models.IntegerField(blank=True)
    citycode = models.BigAutoField(primary_key=True)
    districtcode=models.ForeignKey(State, on_delete=models.CASCADE)
    cityname=models.CharField(max_length=50, blank=True)
    stdcode=models.BigIntegerField()
    status =models.BooleanField(default=True)
    statecode=models.IntegerField(blank=False)
    countrycode=models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['cityname']


class Userinformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    username=models.CharField(max_length=50, blank=False,unique=True)
    employeecode=models.CharField(max_length=50, blank=True)
    isactive =models.BooleanField(default=True)
    user_type =models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    password= models.CharField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['username']


# class Userinformation(AbstractUser):
#     id = models.BigAutoField(primary_key=True)
#     username=models.CharField(max_length=50, blank=False,unique=True)
#     employeecode=models.CharField(max_length=50, blank=True)
#     isactive =models.BooleanField(default=True)
#     user_type =models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField()
#     password= models.CharField(max_length=200, blank=True)
#     USERNAME_FIELD='username'
#     REQUIRED_FIELDS=[]
    
#     class Meta:
#         ordering = ['username']


class UserAuthorization(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid=models.CharField(max_length=50, blank=True)
    fileid=models.IntegerField(blank=False)
    moduleid=models.IntegerField(blank=False)
    userstatus =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['userid']



class Menumaster(models.Model):
    menuid = models.BigAutoField(primary_key=True)
    menucaption=models.CharField(max_length=50, blank=True)
    pos=models.IntegerField(blank=False)

    class Meta:
        ordering = ['menucaption']


class Modelmaster(models.Model):
    id = models.IntegerField(blank=True)
    modelcode = models.BigAutoField(primary_key=True)
    productcode=models.IntegerField(blank=False)
    modelname=models.CharField(max_length=50, blank=True)
    cylinder=models.CharField(max_length=10, blank=True)
    status =models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['modelname']


class File(models.Model):
    fileid = models.BigAutoField(primary_key=True)
    menuid=models.IntegerField(blank=True)
    filemenuname=models.CharField(max_length=50, blank=True)
    filepath=models.CharField(max_length=200, blank=True,default="#")
    menu_icon=models.CharField(max_length=100, blank=True)
    status =models.CharField(blank=True,max_length=10)
    menuseq=models.IntegerField(blank=True)
    element=models.CharField(max_length=300, blank=True)
    sub_menu=models.CharField(max_length=300, blank=True)
    
    class Meta:
        ordering = ['filemenuname']


class FileInternal(models.Model):
    id = models.IntegerField(primary_key=True,blank=True)
    file_name=models.CharField(max_length=200,blank=True)
    file_id=models.BigIntegerField(blank=True)
    file_sub_route_id=models.BigIntegerField(blank=True)
    element=models.CharField(max_length=300, blank=True)
    path=models.CharField(max_length=500,blank=True)



class Stock(models.Model):
    id = models.IntegerField(blank=True)
    stockistcode = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100, blank=True)
    distributorcode=models.CharField(max_length=100, blank=True)
    citycode=models.IntegerField(blank=False)
    mobile = models.CharField(max_length=30, blank=True)
    emailid = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    phoneno = models.CharField(max_length=30, blank=True)
    faxno = models.CharField(max_length=30, blank=True)
    statecode =models.IntegerField(blank=False)
    districtcode =models.IntegerField(blank=False)
    tehsilcode = models.IntegerField(blank=False)
    stockisttype = models.CharField(max_length=50, blank=True)
    status =models.BooleanField(default=False)
    altphoneno =models.CharField(max_length=30, blank=True)
    countrycode = models.IntegerField(blank=False)
    area = models.CharField(max_length=50, blank=True)
    concernperson = models.CharField(max_length=300, blank=True)
    foryear=models.CharField(max_length=30, blank=True)
    appointdate = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
  
    class Meta:
        ordering = ['name']

class Vehicle(models.Model):
    id = models.IntegerField(blank=True)
    transportcode = models.BigAutoField(primary_key=True)
    productcode=models.IntegerField(blank=False)
    vehicleno = models.CharField(max_length=50, blank=False)
    vehiclename = models.CharField(max_length=50, blank=True)
    drivername = models.CharField(max_length=50, blank=True)
    status =models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['vehiclename']

class Transport(models.Model):
    id = models.IntegerField(blank=True)
    transportcode = models.BigAutoField(primary_key=True)
    transportname=models.CharField(max_length=30, blank=True)
    mobileno = models.CharField(max_length=30, blank=True)
    emailid = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    citycode = models.IntegerField(blank=False)
    status =models.BooleanField(default=True)
    alternatephoneno=models.CharField(max_length=15, blank=True)
    statecode=models.IntegerField(blank=False)
    districtcode=models.IntegerField(blank=True)
    faxno=models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    
    class Meta:
        ordering = ['transportname']

class Tehsi(models.Model):
    id = models.IntegerField(blank=True)
    tehsilcode = models.BigAutoField(primary_key=True)
    citycode=models.IntegerField(blank=False)
    tehsilname = models.CharField(max_length=50, blank=False)
    status =models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    
    class Meta:
        ordering = ['tehsilname']

class Employee(models.Model):
    id = models.IntegerField(blank=True)
    employeecode=models.BigAutoField(primary_key=True)
    designationcode=models.IntegerField(blank=False,default=1)
    employeename = models.CharField(max_length=250, blank=False)
    departmentid=models.IntegerField(blank=False)
    phoneno=models.CharField(max_length=10, blank=True)
    mobileno=models.CharField(max_length=10, blank=True)
    emailid=models.CharField(max_length=250, blank=True)
    dateofjoining=models.DateTimeField()
    reportingdesgination=models.IntegerField(blank=True)
    status =models.BooleanField(default=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ['employeename']

class EmployeeArea(models.Model):
    id = models.IntegerField(blank=True)
    employeearea=models.BigAutoField(primary_key=True)
    employeecode=models.CharField(max_length=20)
    reportingemployeecode=models.CharField(max_length=20)
    designationcode = models.IntegerField(blank=True)
    reportingdesignationcode=models.IntegerField(blank=True)
    countrycode=models.IntegerField(blank=True)
    zonecode=models.IntegerField(blank=True)
    zonecode=models.IntegerField(blank=True)
    statecode=models.IntegerField(blank=True)
    areacode=models.IntegerField(blank=True)
    dealercode=models.IntegerField(blank=True)
    distributorcode=models.IntegerField(blank=True)
    districtcode=models.IntegerField(blank=True)
    assigndate=models.IntegerField(blank=True)
    status =models.BooleanField(default=True)    
    
    class Meta:
        ordering = ['reportingemployeecode']
 

   

# CREATE TABLE public.employeearea (
# 	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
# 	employeecode varchar(20) NULL,
# 	reportingemployeecode varchar(20) NULL,
# 	designationcode int4 NULL,
# 	reportingdesignationcode int4 NULL,
# 	countrycode int4 NULL,
# 	zonecode int4 NULL,
# 	statecode int4 NULL,
# 	areacode int4 NULL,
# 	dealercode int4 NULL,
# 	distributorcode int4 NULL,
# 	districtcode int4 NULL,
# 	assigndate date NULL,
# 	status bool NULL,
# 	CONSTRAINT employeearea_pkey PRIMARY KEY (id)
# );






















