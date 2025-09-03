from django.db import models

# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class HOD(models.Model):
#     name = models.CharField(max_length=50)
#     Department = models.OneToOneField(Department, on_delete=models.SET_NULL , null=True)
#     phone = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.name} ({self.Department.name})"

# class Professor(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=50)
#     Department = models.ForeignKey(Department, on_delete=models.SET_NULL , null=True)
#     Subject = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} ({self.Department.name})"

# class Students(models.Model):
#     name = models.CharField(max_length=100)
#     Register_ID = models.CharField(max_length=100, unique=True)
#     Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
#     HOD = models.ForeignKey(HOD, on_delete=models.SET_NULL ,  null=True)
    
#     def __str__(self):
#         return f"{self.name} ({self.Register_ID})"



from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class HOD(models.Model):
    name = models.CharField(max_length=50)
    Department = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.Department.name if self.Department else 'No Department'})"

class Professor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    Subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.Department.name if self.Department else 'No Department'})"

class Students(models.Model):
    name = models.CharField(max_length=100)
    Register_ID = models.CharField(max_length=100, unique=True)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    HOD = models.ForeignKey(HOD, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.Register_ID})"

