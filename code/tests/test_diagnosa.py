import pytest
from app.models import Diagnosa, Gejala
from app import db

# Fungsi login untuk mengotomatisasi proses login
def login(client, username, password):
    """Fungsi untuk melakukan login pada aplikasi."""
    return client.post('/login', data={
        "username": username,
        "password": password
    }, follow_redirects=True)

def test_diagnosa_page_and_submission(client, app, setup_data):
    """Test akses halaman diagnosa dan pengiriman data diagnosa."""
    
    # Login ke sistem
    login(client, "quicktest1", "QuickPass@1234")

    # Akses halaman diagnosa
    response = client.get('/diagnosa')
    
    # Periksa apakah pengalihan terjadi karena login
    assert response.status_code == 200 
    assert b"Diagnosa" in response.data 

    # Pastikan database diagnosa kosong sebelum pengujian
    with app.app_context():
        assert Diagnosa.query.count() == 0 

    # Siapkan gejala untuk pengujian
    gejala_list = Gejala.query.all()
    if not gejala_list:
        pytest.skip("Tidak ada gejala dalam database untuk pengujian.")

    # Kirim data diagnosa dengan gejala yang valid
    response = client.post('/diagnosa', data={
        "nama_kucing": "Kucing A",
         "jenis_kelamin": "jantan",
        "gejala": [gejala_list[0].kode_gejala, gejala_list[1].kode_gejala]  
    }, follow_redirects=True)

    # Verifikasi status code setelah submit
    assert response.status_code == 200  # Pastikan pengiriman data berhasil

    # Verifikasi data diagnosa di database
    with app.app_context():
        diagnosa = Diagnosa.query.first() 
        assert diagnosa is not None
        assert diagnosa.nama_kucing == "Kucing A"
        assert diagnosa.jenis_kelamin == "jantan"
        assert "Penyakit" in diagnosa.hasil_diagnosa 
        assert gejala_list[0].kode_gejala in diagnosa.gejala_dipilih
        assert gejala_list[1].kode_gejala in diagnosa.gejala_dipilih 
