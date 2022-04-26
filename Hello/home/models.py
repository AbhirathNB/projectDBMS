from pickle import FALSE
from django.db import models


# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc1 = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

# class admintest(models.Model):
#     adminfirstname = models.CharField(max_length=255 )
#     adminlastname = models.CharField(max_length=255 )
#     adminemail = models.CharField(max_length=100)
#     adminid = models.CharField(max_length = 20, unique = True, )
#     adminpassword = models.CharField(max_length = 255) 
#     adminmobile = models.CharField(max_length=20)

class admin1(models.Model):
    adminemail = models.CharField(max_length=100, primary_key=True)
    adminfirstname = models.CharField(max_length=255 )
    adminlastname = models.CharField(max_length=255 )
    

class admin2(models.Model):
    adminid = models.CharField(max_length = 100, primary_key=True)
    adminemail = models.CharField(max_length=100)

# only adminid is taken pk since django does not support compostie primary key
class adminmobile(models.Model):
    adminid = models.ForeignKey(admin2, on_delete=models.CASCADE) 
    adminmobile = models.CharField(max_length=20) 

    class Meta:
        unique_together = (('adminid', 'adminmobile'),)

    
class adminidpassword(models.Model):
    adminid = models.ForeignKey(admin2, on_delete=models.CASCADE)
    adminpassword = models.CharField(max_length = 255)

    class Meta:
         unique_together = (('adminid', 'adminpassword'),)

       
class student1(models.Model):
    studentphone = models.CharField(max_length=20, primary_key= True)
    studentfirstname = models.CharField(max_length=255)
    studentlastname = models.CharField(max_length=100)
    
class student2(models.Model):
    studentemail = models.CharField(max_length=255, primary_key= True)
    studentphone = models.CharField(max_length=20)

class student3(models.Model):
    studentid = models.CharField(max_length=20, primary_key= True)
    studentdob = models.DateField()
    studentemail = models.CharField(max_length=255)    
   
class student4(models.Model):
    studentid = models.CharField(max_length=20, primary_key=True)#remove this pk if it doesnt work
    adminid = models.ForeignKey(admin2,on_delete=models.CASCADE)

    class Meta:    
        unique_together = (('studentid', 'adminid'),)
        
class studentidpassword(models.Model):
    studentid = models.ForeignKey(student3, on_delete=models.CASCADE)
    studentpassword = models.CharField(max_length = 255)

    class Meta:
         unique_together = (('studentid', 'studentpassword'),)
    
class exammarklist1(models.Model):
    examid = models.CharField(max_length=20, primary_key=True)
    studentid = models.ForeignKey(student3, on_delete=models.CASCADE)
    marks = models.IntegerField()

    class Meta:    
        unique_together = (('studentid', 'examid'),)
         
class exammarklist2(models.Model):
    examid = models.CharField(max_length=20, primary_key= True)
    subject = models.CharField(max_length=100)
    examdate = models.DateField() 
    
           
class exammarklist3(models.Model):
    examid = models.CharField(max_length=20)
    adminid = models.ForeignKey (admin2, on_delete=models.CASCADE )
    studentid = models.ForeignKey(student3, on_delete=models.CASCADE)

    class Meta:    
        unique_together = (('studentid', 'examid', 'adminid'),)
         
class examinationtype(models.Model):
    examid = models.CharField(max_length=20)
    examtype = models.CharField(max_length=50)

    class Meta:    
        unique_together = (('examid', 'examtype'),)

class attempts(models.Model):
    studentid = models.ForeignKey(student3,on_delete=models.CASCADE)
    examid = models.ForeignKey(exammarklist2, on_delete=models.CASCADE)
    attemptnumber = models.IntegerField()

    class Meta:    
        unique_together = (('studentid', 'examid'),)


    