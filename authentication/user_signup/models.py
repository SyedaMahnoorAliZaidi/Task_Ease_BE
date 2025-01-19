from django.db import models

# Create your models here.

class Expert(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, default="Expert")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cnic = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    domain = models.CharField(max_length=255)
    years_of_experience = models.PositiveIntegerField()
    availability = models.TextField()

    def __str__(self):
        return self.email

class Customer(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10, default="User")
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    cnic = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.email
    



        
# categories = {
#     ('Web Development', 'Web Development'),
#     ('Mobile Development', 'Mobile Development'),
#     ('Graphic Designing', 'Graphic Designing'),
#     ('Digital Marketing', 'Digital Marketing'),
#     ('Content Writing', 'Content Writing'),
#     ('Video Editing', 'Video Editing'),
#     ('SEO', 'SEO'),
#     ('Data Entry', 'Data Entry'),
#     ('Virtual Assistant', 'Virtual Assistant'),
#     ('Customer Support', 'Customer Support'),
#     ('Accounting', 'Accounting'),
#     ('Human Resources', 'Human Resources'),
#     ('Sales', 'Sales'),
#     ('Marketing', 'Marketing'),
#     ('Business Development', 'Business Development'),
#     ('Project Management', 'Project Management'),
#     ('Legal', 'Legal'),
#     ('Other', 'Other'),
# }
# class Skill(models.Model):
#     expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
#     skill = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.PositiveIntegerField()
#     skill_image = models.ImageField(upload_to='images/')
#     category = models.CharField(max_length=255, choices=categories, default="Other")


#     def __str__(self):
#         return self.skill
    


# # THis is orders app models.py file
# # Every expert will have orders that the customers will genrate for hom
# #Below is the model for orders that is associated with expert and customer 

# from django.db import models
# from authentication.user_signup.models import Expert, Customer
# status = {  active: 'Active',}

# class Order(models.Model):
#     expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     delivery_date = models.DateTimeField()
#     status = models.CharField(max_length=255)
#     price = models.PositiveIntegerField()
#     description = models.TextField()
#     order_image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.status