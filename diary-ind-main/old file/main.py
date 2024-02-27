# Impor pustaka web app framework
from flask import Flask, render_template, request, redirect
# Mengimpor pustaka database
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Menghubungkan SQLite, dan Membuat file diary.db
# Konfigurasikan database - 
# deretan kode ini menonaktifkan fungsionalitas yang tidak perlu dan 
# mengatur jalur ke DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Membuat sebuah DB
db = SQLAlchemy(app )
# 1. "Integer" - ketika kita menentukan tipe data ini, 
# kita menentukan bahwa kolom ini hanya akan menerima integer (bilangan bulat)

# 2. Konfigurasi identifikasi "primary_key = True" 
# menyatakan bahwa id memiliki kunci uniknya sendiri

# Setelah kita membuat DB, setiap entri akan memiliki id uniknya sendiri, yang dapat kita gunakan untuk mengakses data dalam entri tersebut!
# Tugas #1. Membuat tabel DB
class Card(db.Model):
    # Membuat kolom
    # id
    id = db.Column(db.Integer, primary_key=True)
    # menetapkan batas 100 karakter, 
    # dan pengaturan the nullable=False menyatakan t=bahwa kolom tidak bisa dikosongkan
    # Judul
    title = db.Column(db.String(100), nullable=False)
    # Deskripsi
    subtitle = db.Column(db.String(300), nullable=False)
    # Teks
    text = db.Column(db.Text, nullable=False)
    # Menghasilkan objek dan id-nya
    def __repr__(self):
        return f'<Card {self.id}>'

# Menjalankan halaman dengan konten
@app.route('/')
def index():
    # Menampilkan objek DB
    # Tugas #2. Menampilkan objek-objek dari DB di index.html
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html',
                           #cards = kartu
                            cards=cards
                           )

# Menjalankan halaman dengan kartu
@app.route('/card/<int:id>')
def card(id):
    # Tugas #2. Menampilkan kartu yang tepat berdasarkan id-nya
    card = Card.query.get(id)

    return render_template('card.html', card=card)

# Menjalankan halaman dan membuat kartu
@app.route('/create')
def create():
    return render_template('create_card.html')

# Formulir kartu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Tugas #2. Buatlah cara untuk menyimpan data dalam DB
        # Tugas #2. Buatlah cara untuk menyimpan data dalam DB
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)

# Baiklah! DB kita telah diprogram! Sekarang di terminal, 
# mari kita jalankan kode untuk membuatnya seperti sebuah file:

# 1. Buka terminal dan ketik 'python' untuk beralih ke bahasa Python

# 2. Sekarang, impor aplikasi dan bd dari utama: >>>from main import app, db

# 3. Setelah proyek kamu mendapatkan folder instance di dalamnya, ketik ini di terminal: >>>app.app_context().push()

# 4. Terakhir, buatlah file db:: >>>db.create_all()
