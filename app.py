from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    template_name = input("Please input template name(cux or index): ") + '.html'
    try:
        return render_template(template_name)
    except:
        return f"Template {template_name} non-exist."

if __name__ == '__main__':
    app.run(debug=True)