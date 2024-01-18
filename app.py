from quart import Quart

app = Quart(__name__)

@app.route("/snippets", methods=["POST"])
def post_snippet():
    pass

@app.get("/snippets")
def get_snippets():
    pass

@app.get("/snippets/<id>")
def get_snippet():
    pass

if __name__ == '__main__':
    app.run(debug=True)