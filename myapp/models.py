from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):
  title=models.CharField('TITLE',max_length=200,blank=True,null=True)
  body=models.TextField('body',blank=True,null=True)

  def str(self) -> str:
      return self.title
  



class Game(models.Model):
    image=models.ImageField('Rasm',upload_to='post/')
    oyinNomi=models.CharField('Name',max_length=100,blank=True,null=True)
    date=models.DateField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    body=models.TextField()
    comentNum=models.ForeignKey('Comentary',on_delete=models.CASCADE)
    author=models.CharField(CustomUser,max_length=100,blank=True,null=True)
    yuklashlarSoni=models.IntegerField('yuklab olinganlar soni',blank=True,null=True)
    like=models.SmallIntegerField('LIke',blank=True,null=True,default=0)
    ball=models.SmallIntegerField('Ball',blank=True,null=True)
    ortachaBal=models.SmallIntegerField('Urtacha ball',blank=True,null=True)
    views=models.IntegerField('Kurganlar',blank=True,null=True)
    version=models.FloatField('Version',blank=True,null=True)


    def str(self) -> str:
      return self.oyinNomi
    
# class Baholar(models.Model):
#     bahoid = models.ForeignKey(Game,on_delete=models.CASCADE)
#     ball=models.SmallIntegerField('Ball')
#     ortachaBal=models.SmallIntegerField('Urtacha ball')
    

    
    


class Comentary(models.Model):
    # game = models.ForeignKey(Game,on_delete=models.CASCADE)
    image = models.ImageField('image',upload_to='post/',default='static/img/authors/8.jpg')
    name=models.CharField('Name',max_length=50,blank=True,null=True)
    date = models.DateField('date',auto_now_add=True)
    email=models.EmailField('Email',blank=True,null=True)
    subject=models.CharField('Subject',max_length=100,blank=True,null=True)
    body=models.TextField()
    commentNum = models.IntegerField('commentaryalar soni',default=0)

    def str(self) -> str:
      return self.name
    



class Turnir(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image=models.ImageField('Rasm',upload_to='post/')
    oyinNomi=models.ForeignKey(Game,on_delete=models.CASCADE)
    startDate=models.DateField('Date',auto_now=True,blank=True,null=True)
    endDate=models.DateField('Date',auto_now=True,blank=True,null=True)
    timesNum=models.SmallIntegerField('timelar soni',blank=True,null=True)
    participants_age=models.CharField('Age',max_length=100,blank=True,null=True)
    turnirhomiysi=models.CharField('Homiy',max_length=200,blank=True,null=True)
    groupNum=models.SmallIntegerField('group num',blank=True,null=True)
    priz1=models.CharField('1-urin',max_length=50,blank=True,null=True)
    priz2=models.CharField('2-urin',max_length=50,blank=True,null=True)
    priz3=models.CharField('3-urin',max_length=50,blank=True,null=True)

    def str(self) -> str:
      return self.name



class Contact(models.Model):
    
    id=models.IntegerField('id', primary_key=True)
    profile_id=models.ForeignKey('Profil',on_delete=models.CASCADE,default=None)
    email=models.EmailField('Email',blank=True,null=True)
    massage=models.CharField('Subject',max_length=100,blank=True,null=True)
    subject=models.TextField('subject',blank=True,null=True)


    def str(self) -> str:
          return self.subject


class Adress1(models.Model):
    # username = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    adres=models.CharField('Adress',max_length=100,blank=True,null=True)
    phone=models.CharField('Phone',max_length=15,blank=True,null=True)
    email=models.EmailField('Email',blank=True,null=True)
    body=models.TextField('body',blank=True,null=True)

    def str(self) -> str:
      return self.email


class Forum(models.Model):
    
    image = models.ImageField('rasm',upload_to='post/',default='static/img/authors/8.jpg')
    name=models.CharField('Name',max_length=50,blank=True,null=True)
    date = models.DateField('date',auto_now_add=True,blank=True,null=True)
    subject = models.CharField('mavzu',max_length=100,blank=True,null=True)
    email=models.EmailField('Email',blank=True,null=True)
    body=models.TextField('body',blank=True,null=True)

    

    def str(self) -> str:
      return self.name
    
    def countForum(self):
        count = Forum.objects.count()
        return count


class Profil(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,default=None)
    image = models.ImageField('profil rasmi',upload_to='post/',auto_created="C:/Users/eldor/OneDrive/Documents/img/authors/rasm.8.jpg")
    # contact = models.ForeignKey(Contact,on_delete=models.CASCADE)













    










