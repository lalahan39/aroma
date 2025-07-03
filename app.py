from flask import Flask, session, render_template, request, jsonify
import os
from oil_data import oil_data_by_symptom

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Render 배포 시 꼭 보안성 강화할 것

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test1')
def test1():
    return render_template('test1.html')

@app.route('/test2')
def test2():
    return render_template('test2.html') 

@app.route('/test3')
def test3():
    return render_template('test3.html') 

@app.route('/test4')
def test4():
    return render_template('test4.html') 

@app.route('/test5')
def test5():
    return render_template('test5.html') 

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/<symptom>')
def show_oils(symptom):
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template('oils.html', symptom=symptom, oils=oils)

@app.route('/result')
def result():
    result_data = {
        '우울': session.get('test1_sum', 0),
        '불안': session.get('test2_sum', 0),
        '불면': session.get('test3_sum', 0),
        '통증': session.get('test4_sum', 0),
        'PTSD': session.get('test5_sum', 0)
    }
    return render_template('result.html', result=result_data)

@app.route("/detail/depression.html")
def depression_detail_depression():
    symptom = "우울"
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template("detail/depression.html", symptom=symptom, oils=oils)

@app.route("/detail/anxiety.html")
def depression_detail_anxiety():
    symptom = "불안"
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template("detail/anxiety.html", symptom=symptom, oils=oils)

@app.route("/detail/insomnia.html")
def depression_detail_insomnia():
    symptom = "불면증"
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template("detail/insomnia.html", symptom=symptom, oils=oils)

@app.route("/detail/pain.html")
def depression_detail_pain():
    symptom = "통증"
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template("detail/pain.html", symptom=symptom, oils=oils)

@app.route("/detail/PTSD.html")
def depression_detail_PTSD():
    symptom = "PTSD"
    oils = oil_data_by_symptom.get(symptom, [])
    return render_template("detail/PTSD.html", symptom=symptom, oils=oils)


@app.route('/submit_sum', methods=['POST'])
def submit_sum():
    data = request.get_json()

    # 모든 key-value를 세션에 저장
    for key, value in data.items():
        session[key] = value
        print(f"세션에 저장됨: {key} = {value}")

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
