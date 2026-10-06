from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to DevOps Mini Project 🚀</h1>
    <p>Automated CI/CD Pipeline using Flask, Docker and GitHub Actions</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)