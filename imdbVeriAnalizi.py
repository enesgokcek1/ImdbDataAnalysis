import pandas as pd
df = pd.read_json("/Users/enessalihgokcek/Desktop/python/imdb_data.json", lines=True)

# 1- Dosya hakkındaki bilgiler
result = df
result = df.columns
result = df.info

# 2- ilk 5 kaydı gösterin
result = df.head()
# 3- ilk 10 kaydı gösterin
result = df.head(10)
# 4- son 5 kaydı gösterin
result = df.tail()
# 5- son 10 kaydı gösterin
result = df.tail(10)
# 6- sadece movie_name kolonunu alın
result = df["movie_name"]
# 7- sadece movie_name kolonunu içeren ilk 5 kaydı alın
result = df["movie_name"].head()
# 8- sadece movie_name ve Rating kolonunu içeren ilk 5 kaydı alın
result = df[["movie_name","rating"]].head()
# 9- sadece movie_name ve Rating kolonunu içeren son 7 kaydı alın
result = df[["movie_name","rating"]].tail(7)
# 10- sadece movie_name ve rating kolonunu içeren ikinci 5 kaydı alın.
result = df[5:10][["movie_name","rating"]].head()
# 11- sadece movie_name ve rating kolonunu içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesinin alınız.
result = df[df["rating"] >= 8.0][["movie_name","rating"]].head(50) #dıştaki df filtrelemek için içteki ise mantıksal true false
# 12- Yayın tarihi 2014 ve 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df["movie_year"] >= 2014) & (df["movie_year"] <= 2015)] [["movie_name","movie_year"]]
# 13- Aktör Cristopher Nolan'ın filmlerini ve puanlarını listele.
result = df[df["director_name"] == "Christopher Nolan"] [["movie_name","rating","director_name"]]
# 14- imdb puanı 8-9 arası türü Sci-Fi olan filmleri listeleyiniz.
result = df[
    (df["rating"] >= 8.0) & (df["rating"] <= 9.0) & (df["movie_year"] >= 2005)
][["movie_name", "rating", "movie_year"]]
print(result)
