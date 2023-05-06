from django.urls import path
from .views import index,community,contact,categories,review,singleBlog,search,category,turnirlar,profil,rasm,sozlamalar,turnirqoshish,turnirupdate,turnirupdate1,turnirdelet1,turnirdelet,profilupdate,profildelet,table,admin1,sms,contactupdate,contactdelet



urlpatterns = [
    
    path('',index,name='index'),
    path('categories/',categories,name='categories'),
    path('community/',community,name='community'),
    path('contact/',contact,name='contact'),
    path('review/',review,name='review'),
    path('singleBlog/<int:id>/',singleBlog,name='singleBlog'),
    path('singleBlog/',singleBlog,name='singleBlog'),
    path('search/',search,name='search'),
    path('category/<int:id>/',category,name='category'),
    path('turnirlar/<int:id>/',turnirlar,name='turnirlar'),
    path('rasm/',rasm,name='rasm'),
    path('profil/<int:id>/',profil,name='profil'),
    path('sozlamalar/',sozlamalar,name='sozlamalar'),
    path('turnirqoshish/',turnirqoshish,name='turnirqoshish'),
    path('turnirupdate/<int:id>/',turnirupdate,name="turnirupdate"),
    path('turnirupdate1/',turnirupdate1,name='turnirupdate1'),
    path('turnirdelet1/',turnirdelet1,name='turnirdelet1'),
    path('turnirdelet/<int:id>/',turnirdelet,name='turnirdelet'),
    path('profilupdate/<int:id>/',profilupdate,name='profilupdate'),
    path('profildelet/<int:id>/',profildelet,name='profildelet'),
    path('table/<int:id>/',table,name='table'),
    path('admin1/',admin1,name='admin1'),
    path('sms/',sms,name='sms'), 
    path('contactupdate/<int:id>/',contactupdate,name='contactupdate'),
    path('contactdelet/<int:id>/',contactdelet,name='contactdelet')
]
