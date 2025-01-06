from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .models import Doctor,Patient,Blogs

from .forms import SignupForm,SignupForm1,LoginForm,NewItemForm

def index(request):
    # items = Item.objects.filter(is_sold=False)[0:6]
    blogs = Blogs.objects.all()
    try:
        
        l=Patient.objects.get(username=str(request.user))
        Pat_status=True
    except:
         Pat_status=False
    print(Pat_status)

    return render(request, 'core/index.html',{'blogs':blogs,'Pat_status':Pat_status})
def your_blogs(request):
    # items = Item.objects.filter(is_sold=False)[0:6]
    blogs = Blogs.objects.filter(Blog_author=str(request.user))
    current_user=request.user
    try:
        
        l=Patient.objects.get(username=str(request.user))
        Pat_status=True
    except:
         Pat_status=False

    return render(request, 'core/blogs2.html',{'blogs':blogs,'current_user':current_user,'Pat_status':Pat_status})
def display_blog(request,Blog_name):
                m=Blogs.objects.all()
                b=0
                print(m)
                for i in m:
                    print(i)
                    print(i.Blog_author,request.user)
                    print(i,Blog_name)
                    if str(i)==str(Blog_name):
                         r=i

                return render(request, 'core/displayblog.html', {
        'blog': r
    })
###################################################################
def self_assesment(request):
                
                return render(request, 'core/selfassesment.html')
def adhd(request):
                
                return render(request, 'core/adhd.html')
def ptsd(request):
                
                return render(request, 'core/ptsd.html')
def depression(request):
                
                return render(request, 'core/depression.html')
def anxiety(request):
                
                return render(request, 'core/anxiety.html')
##################################################################
def blogs(request):
    # items = Item.objects.filter(is_sold=False)[0:6]
    blogs = Blogs.objects.all()
    print(blogs)

    return render(request, 'core/blogs.html',{'blogs':blogs})
def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            print(request.POST.get('username'))
            doc=Doctor()
            doc.username=request.POST.get('username')
            doc.docid=request.POST.get('docid')
            doc.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
#######################################################################################################
def create_blogs(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)

        if form.is_valid():
            try:
                m=Blogs.objects.all()
                b=0
                for i in m:
                    # print(i==request.POST.get('Blog_title'))
                    print(i.Blog_author,request.user)
                    if str(i)==str(request.POST.get('Blog_title')) and str(i.Blog_author)==str(request.user):
                        
                        i.Blog_title=request.POST.get('Blog_title')
                        i.Blog_content=request.POST.get('Blog_content')
                        
                        i.save()
                        b=1
                if b==0:
                    doc=Blogs()
                    doc.Blog_title=request.POST.get('Blog_title')
                    doc.Blog_content=request.POST.get('Blog_content')
                    doc.Blog_author=request.user
                    doc.save()
                

            # form.save()
            except:
                print('addddddddddddddddddddddd')
                doc=Blogs()
                doc.Blog_title=request.POST.get('Blog_title')
                doc.Blog_content=request.POST.get('Blog_content')
                doc.Blog_author=request.user
                doc.save()
            return redirect('/')
    else:
        form = NewItemForm()
    try:
        
        l=Patient.objects.get(username=str(request.user))
        Pat_status=True
    except:
         Pat_status=False

    return render(request, 'core/blogs1.html', {
        'form': form,
        'Pat_status':Pat_status
    })
#####################################################################
def delete_blogs(request,Blog_name):
                m=Blogs.objects.all()
                b=0
                print(m)
                for i in m:
                    print(i)
                    print(i.Blog_author,request.user)
                    print(i,Blog_name)
                    if str(i)==str(Blog_name) and str(i.Blog_author)==str(request.user):
                        # print("jjjjjjjjjj")
                    
                        i.delete()
                        b=1
                return redirect('/')
          
#####################################################################
def choice(request):
    return render(request,'core/choice.html')
def signup1(request):
    pat=1
    if request.method == 'POST':
        form = SignupForm1(request.POST)
        
        if form.is_valid():
            form.save()
            pat=Patient()
            pat.username=request.POST.get('username')
            pat.save()
            

            return redirect('/login/')
    else:
        form = SignupForm1()

    return render(request, 'core/signup1.html', {
        'form': form,
        'pat':pat
    })

def user_logout(request):
    auth.logout(request)
    return redirect('/login')