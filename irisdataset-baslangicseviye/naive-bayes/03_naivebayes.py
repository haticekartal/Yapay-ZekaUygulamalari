
# UYGULAMA 2: Kullanıcıdan çiçek ölçülerini alma

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

iris = load_iris()

X = iris.data
y = iris.target

# Modeli oluşturalım ve eğitelim
model = GaussianNB()
model.fit(X, y)

# Kullanıcıdan ölçüleri alalım
sepal_uzunluk = float(input("Sepal uzunluğunu girin: "))
sepal_genislik = float(input("Sepal genişliğini girin: "))
petal_uzunluk = float(input("Petal uzunluğunu girin: "))
petal_genislik = float(input("Petal genişliğini girin: "))

# Girilen ölçüleri listeye aktaralım
yeni_cicek = [[
    sepal_uzunluk,
    sepal_genislik,
    petal_uzunluk,
    petal_genislik
]]

# Tahmin yapalım
tahmin = model.predict(yeni_cicek)

# Çiçeğin adını bulalım
cicek_adi = iris.target_names[tahmin[0]]

print("Tahmin edilen çiçek türü:", cicek_adi)
