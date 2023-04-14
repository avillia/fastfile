from flask import Blueprint, render_template

upload_bp = Blueprint("upload", __name__)


@upload_bp.get("/")
def show_upload_form():
    return render_template("upload.html")


@upload_bp.post("/")
def process_file_upload():
    ...
