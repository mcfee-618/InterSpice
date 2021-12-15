from logging import log
from django.utils.deprecation import MiddlewareMixin
from InterSpice.settings import logger

class LogMiddleware(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        pass