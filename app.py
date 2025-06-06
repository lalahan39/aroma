from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Render 배포 시 꼭 보안성 강화할 것

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('test.html') 

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
