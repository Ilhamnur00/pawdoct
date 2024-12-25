from app import create_app  # Mengimpor fungsi create_app dari modul app

# Membuat instance aplikasi Flask dengan konfigurasi yang sudah diatur di create_app
app = create_app()

# Menentukan folder untuk file statis (CSS, JS, gambar)
app.static_folder = "static"

# Menjalankan aplikasi jika file ini dieksekusi langsung
if __name__ == '__main__':
    app.run(debug=True)  # Menjalankan server dalam mode debug (berguna untuk pengembangan)
