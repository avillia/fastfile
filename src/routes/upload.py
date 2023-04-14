from flask import Blueprint

upload_bp = Blueprint("upload", __name__)


@upload_bp.get("/")
def show_upload_form():
    ...


@upload_bp.post("/")
def process_file_upload():
    ...
