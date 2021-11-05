import os.path
from django.shortcuts import redirect, render
from django.views import View
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from article.models import Post, Link


class BaseView(View):

    DEFAULT_BACKGROUND_IMAGE = "love.jpg"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__background_image = None

    def set_background_image(self, image_name: str):
        image_path = os.path.join(settings.STATIC_URL, "background", image_name)
        if os.path.isfile(image_path):
            self.__background_image = f"background/{image_name}"
        else:
            self.__background_image = f"background/{self.DEFAULT_BACKGROUND_IMAGE}"

    def render(self, request, template_name, context=None, content_type=None, status=None, using=None):
        if not self.__background_image:
            self.__background_image = f"background/{self.DEFAULT_BACKGROUND_IMAGE}"
        if not context:
            context = {}
        context.update({"background_image": self.__background_image})
        return render(request=request,
                      template_name=template_name,
                      context=context,
                      content_type=content_type,
                      status=status,
                      using=using)


class IndexView(BaseView):
    def get(self, request, *args, **kwargs):
        alert_msg = request.session.pop("alert_msg", None)    
        self.set_background_image("love.jpg")  
        posts = Post.objects
        if not request.user.is_authenticated:
            posts = posts.filter(is_private=0)
        posts = posts.order_by('-timestamp')[:3]
        links = Link.objects.all()
        context = {
            "posts": posts,
            "links": links
        }
        if alert_msg:
            context.update({"alert_msg": alert_msg})
        return self.render(request, 'index.html', context=context)
    
class LoginView(BaseView):
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['alert_msg'] = f"welcome {user.username} success login"
            return redirect(reverse('index'))
        # Redirect to a success page.
        # Return an 'invalid login' error message.
        return redirect(reverse('index'))

class LogoutView(BaseView):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        request.session['alert_msg'] = "success logout"
        return redirect(reverse('index'))
