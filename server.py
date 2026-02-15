from flask import Flask

app = Flask(_name_)

@app.get("/")
def home():
    return "Merhaba! Railway çalışıyor."

if _name_ == "_main_":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
