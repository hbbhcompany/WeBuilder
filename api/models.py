from django.db import models

# Create your models here.

class Message(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  number = models.IntegerField( blank=True, null=True)
  message = models.CharField(max_length=200, blank=True, null=True)
  address = models.CharField(max_length=200, blank=True, null=True)
  jobType = models.CharField(max_length=200, blank=True, null=True)
  adminName = models.CharField(max_length=200, blank=True, null=True)
  workerName = models.CharField(max_length=200, blank=True, null=True)
  orderAccepted = models.CharField(default='NotAccepted',max_length=200, blank=True, null=True, choices=(('Accepted','Accepted'),('NotAccepted','NotAccepted')))
  workerSelected = models.CharField(default='NotAccepted',max_length=200, blank=True, null=True, choices=(('Accepted','Accepted'),('NotAccepted','NotAccepted')))
  workerGone = models.CharField(default='NotAccepted',max_length=200, blank=True, null=True, choices=(('Accepted','Accepted'),('NotAccepted','NotAccepted')))
  workerArrived = models.CharField(default='NotAccepted',max_length=200, blank=True, null=True, choices=(('Accepted','Accepted'),('NotAccepted','NotAccepted')))
  timeArrive = models.CharField(max_length=200, blank=True, null=True)
  def __str__(self):
    return  self.name

class Card(models.Model):
  Options = (
    ('Сантехника', 'Сантехника'),
    ('Электроэнергия','Электроэнергия'),
    ('Связь','Связь'),
    ('Интернетb', 'Интернет'),
    ('Бытовая техника (ремонт)', 'Бытовая техника (ремонт)'),
    ('Чистка / уборка','Чистка / уборка'),
    ('Перемещение (грузчик)','Перемещение (грузчик)'),
    ('Мебель (ремонт/сборка)', 'Мебель (ремонт/сборка)'),
    ('Садоводство', 'Садоводство'),
    ('Малогабаритные грузы','Малогабаритные грузы'),
    ('Крупногабаритные грузы','Крупногабаритные грузы'),
    ('Автокран', 'Автокран'),
    ('Экскаватор', 'Экскаватор'),
    ('Эвакуатор','Эвакуатор'),
    ('Землерой','Землерой'),
    ('Укладка кирпича', 'ИнтеУкладка кирпичарнет'),
    ('Косметика', 'Косметика'),
    ('Штукатурка','Штукатурка'),
    ('Моляр','Моляр'),
    ('Крыша', 'Крыша'),
  )
  
  name = models.CharField(max_length=200, blank=True, null=True)
  number = models.IntegerField( blank=True, null=True)
  jobKind = models.CharField(default='Boshqa Kasb', max_length=200,null=True, choices=Options)

  def __str__(self):
      return self.jobKind
  