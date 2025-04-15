from flask import request, jsonify, Blueprint
import curd

routes_bp = Blueprint('userroute', __name__)


@routes_bp.route('/user', methods=["POST"])
def adduser():
    data = request.get_json()
    result = curd.add_user(data)
    return jsonify(result)


@routes_bp.route('/users', methods=['GET'])
def getusers():
    result = curd.getall_user()
    return jsonify(result)


@routes_bp.route('/userid/<int:user_id>', methods=['GET'])
def getuserbyid(user_id):
    response = curd.get_user(user_id)
    return jsonify(response)


@routes_bp.route('/users/<int:user_id>', methods=["PUT"])
def updateuser(user_id):
    response = request.get_json()
    result = curd.update_user(user_id, **response)
    return jsonify(result)


@routes_bp.route('/userdelete/<int:user_id>', methods=["DELETE"])
def deleteuser(user_id):
    result = curd.delete_user(user_id)
    return jsonify(result)
