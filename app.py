from flask import Flask, flash, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# 🔽 これを追加（セキュリティ上、ランダムで長い値が推奨）
app.secret_key = 'your-secret-key-12345'  # 本番環境では環境変数から設定しましょう
# アップロードフォルダの設定
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



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

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['ccc']
    age = request.form['ddd']
    blood_type = request.form['eee']
    error = None

    if not name or not age or not blood_type:
        error = '全ての項目を入力してください'
    
    return render_template('result.html', name=name, age=age, blood_type=blood_type, error=error)

@app.route('/search')
def search():
    query = request.args.get('q')
    return f'検索ワード: {query}'




@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'ファイルが選択されていません'
        filename = secure_filename(file.filename)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return '許可されていないファイル形式です'

        return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return f'アップロード完了: <br><img src="/static/uploads/{filename}" width="300">'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/gallery')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)


if __name__ == "__main__":
    app.run(debug=True)