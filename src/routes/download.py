from flask import Blueprint

download_bp = Blueprint("download", __name__)


@download_bp.get("/<string:file_id>")
def info_page_for_file(file_id: str):
    ...


@download_bp.get("/<string:file_id>/download")
def perform_downloading(file_id: str):
    ...
