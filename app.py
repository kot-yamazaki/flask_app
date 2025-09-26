from flask import Flask, flash, redirect, request, url_for
from flask import render_template

app = Flask(__name__)

# 🔽 これを追加（セキュリティ上、ランダムで長い値が推奨）
app.secret_key = 'your-secret-key-12345'  # 本番環境では環境変数から設定しましょう


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/services")
def servics():
    return "servicesの画面です"

@app.route('/profile/<username>')
def profile(username):
    a = 19
    hobbies = ['プログラミング', '音楽', '映画鑑賞']
    return render_template('profile.html', username=username, age=a, hobbies=hobbies)

@app.route('/mypage')
def mypage():
    return render_template('mypage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # 確認のためコンソール出力（本番ではデータベースやメール送信処理など）
    print(f"お問い合わせがありました\n名前: {name}\nメール: {email}\n内容: {message}")

    flash("お問い合わせを受け付けました。ありがとうございます。")
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True)