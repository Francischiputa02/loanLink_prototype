import uuid
from django.db import models
from user.models import User


class ClientProfile(models.Model):
    GENDER =(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    empolyee_number = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER, default='Male')
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    credit_score = models.BigIntegerField(blank=True, null=True)
    bank = models.CharField(max_length=200, blank=True, null=True)
    bank_acc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
           return f'{self.email}'

    class Meta:
	
	    db_table = "client_profile"

class AgentProfile(models.Model):
      GENDER =(
          ('Male', 'Male'),
          ('Female', 'Female'),
      )
      agent_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
      first_name = models.CharField(max_length=200)
      last_name = models.CharField(max_length=200)
      phone = models.CharField(max_length=200)
      email = models.EmailField()
      address = models.CharField(max_length=200)
      gender = models.CharField(max_length=200, choices=GENDER, default='Male')
      date_of_birth = models.DateField(blank=True, null=True)
      bank = models.CharField(max_length=200, blank=True, null=True)
      bank_acc = models.CharField(max_length=200, blank=True, null=True)
      date_joined = models.DateField(auto_now_add=True)
      is_active = models.BooleanField(default=True)
      is_agent = models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)

      class Meta:
	      db_table = "agent_profile"

