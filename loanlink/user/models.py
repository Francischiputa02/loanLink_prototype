import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
	
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

	def create_client(self,email,password):
		if password is None:
			raise TypeError('Client must have a password')
		user = self.create_user(email,password)
		user.is_client = True
		user.save()
		return user


	def create_agent(self,email,password):
		if password is None:
			raise TypeError('Agent must have a password')
		user = self.create_user(email,password)
		user.is_agent = True
		user.save()
		return user
		
class User(AbstractBaseUser):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
	is_agent = models.BooleanField(default=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	# Tells Django that the UserManager class defined above should manage
	# objects of this type.
	objects = UserManager()

	def __str__(self):
		return self.email

class Meta:
	'''
	to set table name in database
	'''
	db_table = "login"
