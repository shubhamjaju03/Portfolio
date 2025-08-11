from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Configuration ---
# 🔐 Never hardcode secrets in production (this is for development only)
app.config['SECRET_KEY'] = 'your-very-secret-key'

# Email Config (using Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'shubhamjaju03@gmail.com'  # Your Gmail
app.config['MAIL_PASSWORD'] = 'bxtmqgpdrtrpjenl'        # NOT your Gmail password!
app.config['MAIL_DEFAULT_SENDER'] = ('Shubham Jaju Portfolio', 'shubhamjaju03@gmail.com')

# Initialize Flask-Mail

# --- Routes ---
@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(debug=True)