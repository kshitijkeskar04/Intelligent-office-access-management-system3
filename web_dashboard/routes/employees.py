from flask import Blueprint, request, jsonify
import os

emp_bp = Blueprint('employees', __name__)

@emp_bp.route('/', methods=['GET'])
def get_employees():
    # Return list of employees
    employees = []
    for filename in os.listdir("../../data/employees"):
        if filename.endswith(".jpg"):
            employees.append({
                "id": filename.split(".")[0],
                "image": filename
            })
    return jsonify(employees)

@emp_bp.route('/', methods=['POST'])
def add_employee():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
        
    file = request.files['file']
    emp_id = request.form.get('emp_id')
    
    if file and emp_id:
        filename = f"{emp_id}.jpg"
        file.save(os.path.join("../../data/employees", filename))
        return jsonify({"status": "success"})
    
    return jsonify({"error": "Invalid data"}), 400