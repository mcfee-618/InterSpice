import uuid
from datetime import datetime



def get_filename(filename, request):
    """
    重命名上传文件的名字及路径
    """
    file_format = filename.split(".")[1]
    now = datetime.now()
    year = now.year
    datetime_str = f"{now.month}_{now.day}"
    random_str = str(uuid.uuid4()).replace('_', "").replace('-', '')[:16]
    filename = f"{year}/{datetime_str}-{random_str}.{file_format}"
    referrer = request.META.get('HTTP_REFERER')
    models = {"post", "userprofile"}
    for model in models:
        if model in referrer:
            return f"{model}/{filename}"
    return filename
