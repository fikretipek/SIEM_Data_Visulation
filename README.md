# SIEM Veri Görselleştirme

Bu depo, Python kullanarak **SIEM ve güvenlik ile ilgili verilerin görsel analizine** odaklanmaktadır.
Amaç, yapılandırılmış ve yarı yapılandırılmış güvenlik günlüklerini, tespit mühendisliğini, tehdit avcılığını ve SOC karar alma süreçlerini destekleyen **yorumlanabilir görsel kalıplara** dönüştürmektir.

Proje, **kategorik ağ ve güvenlik verilerinin** nasıl kodlanabileceğini, analiz edilebileceğini ve görselleştirilebileceğini göstererek, ham günlükler aracılığıyla kolayca gözlemlenemeyen ilişkileri, davranışları ve anormallikleri ortaya çıkarır.

## 📌 Kapsam ve Amaçlar

- SIEM benzeri ağ trafiği verilerinin görsel olarak incelenmesi
- Çoklu kategorik boyutlarda desen analizi
- Aşağıdaki gibi SOC kullanım durumlarına destek:

- Davranışsal analiz

- Anomali tespiti hazırlığı

- Tespit mühendisliği içgörüleri

- Tehdit avlama hipotezi oluşturma

## 📊 Temel Kavramlar

Bu depo aşağıdaki kavramları uygulamaktadır:

- Güvenlik günlükleri için kategorik veri kodlaması
- Çok boyutlu görselleştirme teknikleri
- Günlük öznitelikleri arasında desen ve ilişki keşfi
- SOC ve SIEM iş akışları için veri odaklı destek

## 🛠️ Kullanılan Teknolojiler

- **Python**
- **Pandas** – veri işleme ve ön işleme
- **Scikit-learn** – kategorik kodlama
- **Plotly** – etkileşimli, çok boyutlu görselleştirmeler

## 📂 Depo İçindekiler

```metin
SIEM_Veri_Görselleştirme/
│
├── fake_network_traffic.csv
├── fake_network_traffic - dummy data.py
├── traffic_pattern_visualization(multi_color).py
├── README.md
