from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tag_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tags():
    print("Creating tags...")
    # Logic to create tagsp
    print(request.json)
    return jsonify({"message": "Tags created successfully"}), 201