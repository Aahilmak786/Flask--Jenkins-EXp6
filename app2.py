from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    name = "Aahil Momin"
    app_id = "2410181"

    return f"""
    <h1>Welcome to My Flask App</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>App ID:</strong> {app_id}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)