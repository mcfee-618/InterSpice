import os.path
from django.shortcuts import render
from django.views import View
from django.conf import settings


class BaseView(View):

    DEFAULT_BACKGROUND_IMAGE = "default.jpg"

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
        self.set_background_image("default.jpg")
        return self.render(request, 'index.html')
