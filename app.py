from flask import Flask, request, jsonify
import openai
import base64

app = Flask(__name__)

# Apna OpenAI API key yahan dalna
openai.api_key = "YOUR_API_KEY"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["panel"]
    image_bytes = file.read()
    b64_image = base64.b64encode(image_bytes).decode("utf-8")

    # OpenAI Vision se script banwana
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": "Explain this manhwa panel as a cinematic script in simple Hindi with some English words."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}}
            ]}
        ]
    )

    script = response.choices[0].message["content"]
    return jsonify({"script": script})

if __name__ == "__main__":
    app.run(debug=True)