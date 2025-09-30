# 📊 Sentiment Analysis of Gojek App Reviews  

This project performs **sentiment analysis** on user reviews of the **Gojek application** from Google Play Store.  
The goal is to classify user perceptions into **positive** and **negative** categories using **NLP** and **Deep Learning (LSTM)**.  

---

## 🛠️ Technologies Used  
- **Python 3.13**  
- **Pandas**, **NumPy** → Data processing  
- **NLTK**, **Sastrawi** → Text preprocessing (tokenizing, stopwords, stemming, lemmatization)  
- **Scikit-learn** → Train-test split, evaluation metrics, label encoding 
- **Matplotlib, Seaborn, WordCloud** → Data visualization  
- **google-play-scraper** → Scraping reviews from Google Play  
- **TensorFlow / Keras** → LSTM model for sentiment classification  

---

## 📑 Workflow  

### 1. Data Collection  
Reviews were scraped from Google Play using `google-play-scraper` and saved as `gojek_reviews.csv`.  

### 2. Preprocessing  
- Cleaning → remove numbers, links, mentions, hashtags, punctuation  
- Case folding → lowercase transformation  
- Slangword normalization → replace informal/slang words with standard Indonesian  
- Tokenizing → split text into tokens  
- Stopword removal → remove common Indonesian and English stopwords  
- Stemming & Lemmatization →  
  - Indonesian → Sastrawi stemmer  
  - English → WordNet lemmatizer  

### 3. Lexicon-based Sentiment Scoring (baseline)  
Lexicon dictionaries (positive & negative words) were used to assign sentiment scores.  

### 4. Feature Engineering for Deep Learning  
- Convert text into sequences using **Tokenizer**  
- Pad sequences to fixed length (`max_len=100`)  

### 5. Modeling (LSTM)  
- **Embedding Layer**: maps words into dense vectors  
- **LSTM Layer**: captures sequential dependencies in reviews  
- **Dense Layer** with sigmoid activation: binary classification (positive/negative)  

### 6. Evaluation  
- Confusion Matrix  
- Precision, Recall, F1-score  
- Accuracy  

---

## 📊 Results  
- **LSTM model (5 epochs, batch_size=64):**  
  - Accuracy: ~95% on test set (with ~13,700 balanced reviews)  
  - Strong performance on both positive and negative classes  

---