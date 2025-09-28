from google_play_scraper import reviews, Sort
import pandas as pd

result, _ = reviews(
    'com.gojek.app',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=1000
)

df = pd.DataFrame(result)
df = df[['content', 'score']]
df.to_csv('gojek_reviews.csv', index=False)

