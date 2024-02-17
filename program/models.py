from django.db import models

#Create your models.

class Courses(models.Model):
     name=models.CharField(max_length=100)
     description = models.TextField(null=True,blank=True)
     images = models.ImageField(upload_to='courses/',blank=True,null=True)   
     totalyear = models.SmallIntegerField(null=True,blank=True) 

     def __str__(self):
         return self.name
     

class BBAFeeStructureYear1(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    Admission_Fee = models.BigIntegerField(max_length =200)
    Annual_Fee = models.BigIntegerField(null=True, blank=True)
    First_Aid = models.BigIntegerField(null=True, blank=True)
    Student_Welfare_fund = models.BigIntegerField(null=True, blank=True)
    Admission_Form_fee = models.BigIntegerField(null=True, blank=True)
    Id_card  = models.BigIntegerField(max_length=50, null=True, blank=True)
    Exam_Fee = models.BigIntegerField(null=True,blank=True)
    Tie_Fee	= models.BigIntegerField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)


    def __str__(self):
        return str(self.Admission_Fee)
    
    @property
    def get_total(self):
            if self.Admission_Fee is not None and self.Annual_Fee is not None and self.Annual_Fee is not None and self.First_Aid is not None and self.Student_Welfare_fund is not None and self.Admission_Form_fee is not None and self.Id_card is not None and self.Exam_Fee is not None and self.Tie_Fee is not None:
                return self.Admission_Fee + self.Annual_Fee + self.First_Aid + self.Student_Welfare_fund + self.Admission_Form_fee + self.Id_card + self.Exam_Fee + self.Tie_Fee
            return 0
    
class BBAFeeStructureYear2(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    Admission_Fee = models.BigIntegerField(max_length =200)
    Annual_Fee = models.BigIntegerField(null=True, blank=True)
    First_Aid = models.BigIntegerField(null=True, blank=True)
    Student_Welfare_fund = models.BigIntegerField(null=True, blank=True)
    Admission_Form_fee = models.BigIntegerField(null=True, blank=True)
    Id_card  = models.BigIntegerField(max_length=50, null=True, blank=True)
    Exam_Fee = models.BigIntegerField(null=True,blank=True)
    Tie_Fee	= models.BigIntegerField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)


    def __str__(self):
        return str(self.Admission_Fee)
    
    @property
    def get_total(self):
        if self.Admission_Fee is not None and self.Annual_Fee is not None and self.Annual_Fee is not None and self.First_Aid is not None and self.Student_Welfare_fund is not None and self.Admission_Form_fee is not None and self.Id_card is not None and self.Exam_Fee is not None and self.Tie_Fee is not None:
            return self.Admission_Fee + self.Annual_Fee + self.First_Aid + self.Student_Welfare_fund + self.Admission_Form_fee + self.Id_card + self.Exam_Fee + self.Tie_Fee
        return 0
    

class BBAFeeStructureYear3(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    Admission_Fee = models.BigIntegerField(max_length =200)
    Annual_Fee = models.BigIntegerField(null=True, blank=True)
    First_Aid = models.BigIntegerField(null=True, blank=True)
    Student_Welfare_fund = models.BigIntegerField(null=True, blank=True)
    Admission_Form_fee = models.BigIntegerField(null=True, blank=True)
    Id_card  = models.BigIntegerField(max_length=50, null=True, blank=True)
    Exam_Fee = models.BigIntegerField(null=True,blank=True)
    Tie_Fee	= models.BigIntegerField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)

    

    def __str__(self):
        return str(self.Admission_Fee)
    
    @property
    def get_total(self):
            if self.Admission_Fee is not None and self.Annual_Fee is not None and self.Annual_Fee is not None and self.First_Aid is not None and self.Student_Welfare_fund is not None and self.Admission_Form_fee is not None and self.Id_card is not None and self.Exam_Fee is not None and self.Tie_Fee is not None:
                return self.Admission_Fee + self.Annual_Fee + self.First_Aid + self.Student_Welfare_fund + self.Admission_Form_fee + self.Id_card + self.Exam_Fee + self.Tie_Fee
            return 0


class BBAFeeStructureYear4(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    Admission_Fee = models.BigIntegerField(max_length =200)
    Annual_Fee = models.BigIntegerField(null=True, blank=True)
    First_Aid = models.BigIntegerField(null=True, blank=True)
    Student_Welfare_fund = models.BigIntegerField(null=True, blank=True)
    Admission_Form_fee = models.BigIntegerField(null=True, blank=True)
    Id_card  = models.BigIntegerField(max_length=50, null=True, blank=True)
    Exam_Fee = models.BigIntegerField(null=True,blank=True)
    Tie_Fee	= models.BigIntegerField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)


    def __str__(self):
        return str(self.Admission_Fee)
    
    @property
    def get_total(self):
            if self.Admission_Fee is not None and self.Annual_Fee is not None and self.Annual_Fee is not None and self.First_Aid is not None and self.Student_Welfare_fund is not None and self.Admission_Form_fee is not None and self.Id_card is not None and self.Exam_Fee is not None and self.Tie_Fee is not None:
                return self.Admission_Fee + self.Annual_Fee + self.First_Aid + self.Student_Welfare_fund + self.Admission_Form_fee + self.Id_card + self.Exam_Fee + self.Tie_Fee
            return 0
    

class BBSFeeStructureYear1(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    Admission_Fee = models.BigIntegerField(max_length =200)
    Annual_Fee = models.BigIntegerField(null=True, blank=True)
    First_Aid = models.BigIntegerField(null=True, blank=True)
    Student_Welfare_fund = models.BigIntegerField(null=True, blank=True)
    Admission_Form_fee = models.BigIntegerField(null=True, blank=True)
    Id_card  = models.BigIntegerField(max_length=50, null=True, blank=True)
    Exam_Fee = models.BigIntegerField(null=True,blank=True)
    Tie_Fee	= models.BigIntegerField(null=True,blank=True)
    pdf_file = models.FileField(upload_to='pdf_files/', null=True, blank=True)


    def __str__(self):
        return str(self.Admission_Fee)
    
    @property
    def get_total(self):
            if self.Admission_Fee is not None and self.Annual_Fee is not None and self.Annual_Fee is not None and self.First_Aid is not None and self.Student_Welfare_fund is not None and self.Admission_Form_fee is not None and self.Id_card is not None and self.Exam_Fee is not None and self.Tie_Fee is not None:
                return self.Admission_Fee + self.Annual_Fee + self.First_Aid + self.Student_Welfare_fund + self.Admission_Form_fee + self.Id_card + self.Exam_Fee + self.Tie_Fee
            return 0

    
    


