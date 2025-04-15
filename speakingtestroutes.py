from flask import request, jsonify, Blueprint
import curd

routes_bp = Blueprint('speakingtest', __name__)


@routes_bp.route('/addspeakingtest', methods=['POST'])
def addspeakingtest():
    data = request.get_json()
    result = curd.add_Speakingtest(data)
    return jsonify(result)


@routes_bp.route('/getall_speakingtest', methods=['GET'])
def getallspeakingtest():
    result = curd.selectall_Speakingtest()
    return jsonify(result)


@routes_bp.route('/getbyid_speakingtest/<int:user_id>', methods=['GET'])
def getidspeakingtest(user_id):
    result = curd.select_Speakingtest(user_id)
    return jsonify(result)


@routes_bp.route('/update_speakingtest/<int:user_id>', methods=['PUT'])
def updatespeakingtest(user_id):
    data = request.get_json()
    data.pop("user_id", None)
    result = curd.update_Speakingtest(user_id, **data)
    return jsonify(result)


@routes_bp.route('/delete_speakingtest/<int:user_id>', methods=['DELETE'])
def deletespeakingtest(user_id):
    result = curd.delete_Speakingtest(user_id)
    return jsonify(result)
