from flask.views import MethodView
from ..utils.storage import storage
import uuid
from flask import request

class MediaStorage(MethodView): #/files/put_url
    def get (self,file_format):
        #file_format = request.args.get('file_format')
        file_name = f'{uuid.uuid4().hex}.{file_format}'
        url = storage.put_url(file_key=file_name)

        return {'media_url': url,'file_name': file_name},200