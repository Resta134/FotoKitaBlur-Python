# 📸 Trend Foto Kita Blur (Python)

Project ini adalah implementasi Computer Vision menggunakan Python untuk mengikuti tren "Foto Kita Blur". Memanfaatkan deteksi *landmark* tangan untuk memberikan efek blur secara dinamis pada *feed* webcam secara *real-time*.

## 🛠️ Teknologi yang Digunakan
* **Python 3.x**
* **OpenCV** (`opencv-python`) - Untuk pemrosesan gambar dan akses antarmuka webcam.
* **MediaPipe** (`mediapipe`) - Untuk deteksi *landmark* tangan menggunakan model `hand_landmarker.task`.

## 📂 Struktur File
* `trend_blur.py` : Script utama yang berisi logika untuk menjalankan program dan deteksi kamera.
* `hand_landmarker.task` : Model *Machine Learning* bawaan dari MediaPipe untuk mendeteksi pergerakan atau titik-titik pada tangan.

## 🚀 Cara Instalasi & Menjalankan Program

### 1. Clone Repository
Unduh project ini ke komputer kamu dan masuk ke dalam foldernya:
```bash
git clone [https://github.com/Resta134/FotoKitaBlur-Python.git](https://github.com/Resta134/FotoKitaBlur-Python.git)
cd FotoKitaBlur-Python
```

### 2. Install Library (Dependencies)
Jalankan perintah berikut untuk mengunduh library yang dibutuhkan:
```bash
pip install opencv-python mediapipe
```

### 3. Jalankan Program
Pastikan webcam laptop kamu aktif dan tidak sedang digunakan oleh aplikasi lain (seperti Zoom/GMeet), lalu jalankan script utamanya:
```bash
python trend_blur.py
```
