from logging import _levelToName
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from InterSpice.connections import get_redis_connection
from InterSpice.settings import logger
from datetime import datetime



class RateLimitMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        return
        if request.user.is_authenticated:
            return
        date_str = datetime.now().strftime("%Y-%m-%d-%H")
        redis_key = "%s:%s" % ("ratelimit", date_str)
        client_ip = request.META["REMOTE_ADDR"]
        redis_conn = get_redis_connection()
        pipe = redis_conn.pipeline(transaction=False)
        pipe.hincrby(redis_key, client_ip, 1)
        pipe.expire(redis_key, 1800)
        result = pipe.execute()
        count = result[0]
        if count > 10:
            logger.info(f"ip {client_ip} visit {count} in {date_str}")
            return HttpResponse("您的访问频率挺高的，喜欢我们么？")
            
