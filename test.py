from flask import Flask

app = Flask(__name__)

# Pass the required route to the decorator.




@app.route("/")
def index():
	return "Homepage of GeeksForGeeks"


if __name__ == "__main__":
	app.run()
