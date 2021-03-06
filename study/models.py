from django.db import models

# Create your models here.

SUBJECT_CHOICES = (
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('Others', 'Others'),
)

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=10, default='')
    query = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

class CLass_1(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_1/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_2(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_2/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_3(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_3/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_4(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_4/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_5(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_5/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_6(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_6/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_7(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_7/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_8(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_8/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_9(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_9/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name

class CLass_10(models.Model):
    s_no = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_upload = models.FileField(upload_to='class_10/', blank=True, default='')
    subject = models.CharField(choices=SUBJECT_CHOICES, default='Maths', max_length=20)
    file_link = models.URLField(max_length=600, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-timestamp']

    def __str__(self):
        return self.file_name
