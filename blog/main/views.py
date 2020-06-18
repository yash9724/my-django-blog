from django.shortcuts import render, get_object_or_404, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .models import Post
from .forms import EmailForm

# Create your views here.



# def post_list(request):
#     posts = Post.published.all()
#     paginator = Paginator(posts, 4) 
#     page_number = request.GET.get('page')
    
#     try:
#         page_obj = paginator.page(page_number)
#     except PageNotAnInteger:
#         # page_obj = paginator.page(1)
#         raise Http404()
#     except EmptyPage:
#         raise Http404()
#         # page_obj = paginator.page(paginator.num_pages)

#     return render(request,
#                   'main/post/list.html',
#                    {'page_obj':page_obj}
#                 )

class PostListView(ListView):
    queryset =  Post.published.all()
    paginate_by = 4
    template_name = 'main/post/list.html'
    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                            status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    return render(request,
                'main/post/detail.html',
                {'post':post})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'vikusingh210@xyz.com', [cd['to']])
            sent = True
    else:
        form = EmailForm()
    return render(request, 'main/post/share.html', {'post':post,
                                                    'form':form,
                                                    'sent' : sent})
