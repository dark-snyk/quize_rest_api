from flask import Blueprint
from typing import Dict, List
from database.userservice import register_user_db

registration_bp = Blueprint("registration", __name__)

# request to registration
@registration_bp.route("/register/<string:name>/<string:number>", methods=["POST"])
def register_user(name: str, number: str) -> Dict[str, int]:
    user_id = register_user_db(name, number)

    return {'status': 1, 'user_id': user_id}