
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new

from .forms import PostForm # new
from .models import Post

class HomePageView(ListView):
  
    model = Post
    print("Post",Post)
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
    
    
def my_view(request):

    if request.method == 'POST':
        print ('yesssss')

        # form = MyForm(request.POST)

        # print form['my_field'].value()
        # print form.data['my_field']

        # if form.is_valid():

        #     print form.cleaned_data['my_field']
        #     print form.instance.my_field

        #     form.save()
        #     print form.instance.id  # now this one can access id/pk