from flask import Blueprint
from app.storages.controllers import MediaStorage

storage_api = Blueprint('storage_api', __name__)

storage_api.add_url_rule('/files/put_url/<string:file_format>', view_func=MediaStorage.as_view('put_url'), methods=['GET'])