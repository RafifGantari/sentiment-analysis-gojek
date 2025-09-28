# 📊 Sentiment Analysis Aplikasi Gojek

Proyek ini melakukan **analisis sentimen** pada ulasan pengguna aplikasi **Gojek** dari Google Play Store.  
Tujuan utamanya adalah mengetahui persepsi pengguna (positif/negatif) berdasarkan ulasan mereka, menggunakan **Natural Language Processing (NLP)** dan **Machine Learning**.

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.13**
- **Pandas**, **NumPy** → data processing
- **NLTK**, **Sastrawi** → preprocessing teks (tokenizing, stopwords, stemming)
- **Scikit-learn** → TF-IDF, Logistic Regression, SVM, Ensemble
- **Imbalanced-learn (SMOTE)** → balancing dataset
- **Matplotlib, Seaborn, WordCloud** → visualisasi data
- **google-play-scraper** → scraping ulasan dari Google Play

---

## 📑 Langkah Analisis
1. **Scraping Data**  
   Mengambil ulasan aplikasi Gojek dari Google Play Store menggunakan `google-play-scraper`.

2. **Preprocessing Teks**  
   - Cleaning (hapus angka, simbol, URL, mention, dsb)  
   - Case folding (lowercase)  
   - Tokenizing  
   - Stopwords removal (Indonesia & Inggris)  
   - Stemming (Sastrawi)  
   - Slangword normalization  

3. **Feature Extraction**  
   Menggunakan **TF-IDF Vectorizer** untuk mengubah teks menjadi vektor numerik.

4. **Modeling**  
   - Logistic Regression  
   - SVM (Support Vector Machine)

5. **Evaluation**  
   - Confusion Matrix  
   - Precision, Recall, F1-Score  
   - Accuracy

---

## 📊 Hasil Model
- Logistic Regression: **Accuracy test ~84.5%**
- Linear SVM (tuned): **Accuracy test ~88%**

Model **Linear SVM (tuned)** memberikan hasil paling stabil dengan akurasi yang cukup baik.

---

## 📥 Cara Menjalankan

### 1. Clone Repo
```bash
git clone https://github.com/RafifGantari/sentiment-analysis-gojek.git
cd sentiment-analysis-gojek
