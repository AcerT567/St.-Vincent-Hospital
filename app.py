from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    hospital_name = "St. Vincent Hospital"
    return render_template('index.html', hospital_name=hospital_name)

if __name__ == '__main__':
    app.run(debug=True)
