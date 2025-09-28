# 📊 Sentiment Analysis of Gojek Application

This project performs **sentiment analysis** on user reviews of the **Gojek** application from the Google Play Store.  
The main goal is to understand user perception (positive/negative) based on their reviews, using **Natural Language Processing (NLP)** and **Machine Learning**.

---

## 🛠️ Technologies Used
- **Python 3.13**
- **Pandas**, **NumPy** → data processing
- **NLTK**, **Sastrawi** → text preprocessing (tokenizing, stopwords, stemming)
- **Scikit-learn** → TF-IDF, Logistic Regression, SVM, Ensemble
- **Imbalanced-learn (SMOTE)** → dataset balancing
- **Matplotlib, Seaborn, WordCloud** → data visualization
- **google-play-scraper** → scraping reviews from Google Play

---

## 📑 Analysis Workflow
1. **Data Scraping**  
   Extracting Gojek app reviews from the Google Play Store using `google-play-scraper`.

2. **Text Preprocessing**  
   - Cleaning (remove numbers, symbols, URLs, mentions, etc.)  
   - Case folding (lowercasing)  
   - Tokenizing  
   - Stopwords removal (Indonesian & English)  
   - Stemming (Sastrawi)  
   - Slangword normalization  

3. **Feature Extraction**  
   Converting text into numerical vectors using **TF-IDF Vectorizer**.

4. **Modeling**  
   - Logistic Regression  
   - SVM (Support Vector Machine)

5. **Evaluation**  
   - Confusion Matrix  
   - Precision, Recall, F1-Score  
   - Accuracy

---

## 📊 Model Results
- Logistic Regression: **Test Accuracy ~88.3%**
- Linear SVM (tuned): **Test Accuracy ~89.7%**

The **tuned Linear SVM** model achieved the most stable and reliable performance with good accuracy.

---

## 📥 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/RafifGantari/sentiment-analysis-gojek.git
cd sentiment-analysis-gojek
