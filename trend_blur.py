import cv2
from cvzone.HandTrackingModule import HandDetector

# 1. Menyalakan Kamera (Angka 0 biasanya untuk webcam bawaan laptop)
cap = cv2.VideoCapture(0)

# 2. Menyiapkan AI Pendeteksi Tangan
# detectionCon=0.8 artinya AI harus yakin 80% bahwa itu benar-benar tangan
detector = HandDetector(detectionCon=0.8, maxHands=1)

print("Kamera menyala! Tunjukkan gaya V/Peace ke kamera.")
print("Tekan tombol 'q' di keyboard untuk menutup program.")

while True:
    # 3. Membaca gambar dari kamera frame per frame
    success, img = cap.read()
    
    # Membalikkan gambar agar seperti cermin (lebih nyaman dilihat)
    img = cv2.flip(img, 1)

    # 4. Mendeteksi tangan di layar
    # draw=False agar garis-garis skeleton AI tidak ikut digambar di tanganmu
    hands, img = detector.findHands(img, draw=False)

    # 5. Logika Utama (If/Else)
    if hands:
        # Ambil data dari tangan pertama yang terdeteksi
        hand1 = hands[0]
        
        # Mengecek jari mana saja yang sedang berdiri
        fingers = detector.fingersUp(hand1)
        
        # 'fingers' akan menghasilkan urutan: [Jempol, Telunjuk, Tengah, Manis, Kelingking]
        # 1 berarti berdiri, 0 berarti ditutup.
        # Jika hanya Telunjuk dan Tengah yang berdiri (Gaya Peace):
        if fingers == [0, 1, 1, 0, 0]:
            # Berikan efek blur yang tebal pada gambar
            img = cv2.GaussianBlur(img, (55, 55), 0)

    # 6. Menampilkan hasil gambar ke layar monitor
    cv2.imshow("Trend Blur 2 Jari", img)

    # 7. Cara menghentikan program (Tekan 'q' di keyboard)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Membersihkan sistem setelah program selesai
cap.release()
cv2.destroyAllWindows()