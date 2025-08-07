from flask import Flask
from routes.employees import emp_bp
from routes.auth import auth_bp
from routes.camera import camera_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key in production

# Register blueprints
app.register_blueprint(emp_bp, url_prefix='/employees')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(camera_bp, url_prefix='/camera')

@app.route('/')
def home():
    return "Office Access System Dashboard"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)  # debug=False to avoid double launch