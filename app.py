from quart import Quart, request, jsonify
import json
app = Quart(__name__)

f = open('data.json')
data = json.load(f)

@app.route("/snippets", methods=["POST"])
async def post_snippet():
    new_data = await request.get_json()

    if not new_data.get("language")  or not new_data.get("code"):
        return jsonify({"error": "missing language or code"}), 400

    new_id = data[-1]["id"] + 1

    id = new_id 
    language = new_data.get("language")
    code = new_data.get("code")

    new_snip = {
        "id": id,
        "language": language,
        "code": code
    }

    data.append(new_snip)

    return jsonify({"message": "new snippet added"}), 200

@app.get("/snippets")
async def get_snippets():
    if not data:
        return jsonify({"error": "not data found"}), 404
    return jsonify({"data": data}), 200

@app.get("/snippets/<int:id>")
async def get_snippet(id):
    snippet = [item for item in data if item["id"] is id]
    print(snippet)
    return jsonify({"data": snippet})


if __name__ == '__main__':
    app.run(debug=True)