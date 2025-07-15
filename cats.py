from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Nyan Cat Video</title>
</head>
<body>
    <h1>Enjoy the Nyan Cat!</h1>
    <video width="640" height="360" controls autoplay loop muted>
        <source src="https://archive.org/download/NyanCat_512/nyan_cat_512kb.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <p>By using this site, you agree to our <a href="/privacy">privacy policy</a>.</p>
</body>
</html>
"""

@app.route('/')
def home():
    ip = request.remote_addr
    print(f"[{datetime.now()}] Visitor IP: {ip}")
    return render_template_string(HTML_PAGE)

@app.route('/privacy')
def privacy():
    return """
    <h2>Privacy Policy</h2>
    <p>We collect your IP address for basic analytics and security. By using this site, you consent to this collection.</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
