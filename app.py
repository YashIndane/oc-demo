from flask import Flask, render_template

app = Flask("my-app")

@app.route("/home")
def homepage():
  return render_template

if __name__ == "__main__":
  app.run(host="localhost", port=2300)
