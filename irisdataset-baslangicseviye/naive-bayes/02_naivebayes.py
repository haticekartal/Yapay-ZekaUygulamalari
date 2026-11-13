
# UYGULAMA 1: Birden fazla çiçeğin türünü tahmin etme

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

# Veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Naive Bayes modelini oluşturalım
model = GaussianNB()

# Modeli eğitelim
model.fit(X, y)

# Üç farklı çiçeğin ölçüleri
yeni_cicekler = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.5, 3.0, 5.8, 2.2]
]

# Çiçek türlerini tahmin edelim
tahminler = model.predict(yeni_cicekler)

# Sonuçları ekrana yazdıralım
for i in range(3):
    cicek_adi = iris.target_names[tahminler[i]]
    print(i + 1, ". çiçeğin türü:", cicek_adi)
