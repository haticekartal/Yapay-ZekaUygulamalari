
# UYGULAMA: Iris veri setiyle Naive Bayes sınıflandırması

# Gerekli kütüphaneleri içe aktaralım
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# Iris veri setini yükleyelim
iris = load_iris()

# Çiçeklerin özelliklerini ve türlerini ayıralım
X = iris.data
y = iris.target

# Verileri %80 eğitim ve %20 test olarak ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Naive Bayes modelini oluşturalım
model = GaussianNB()

# Modeli eğitim verileriyle eğitelim
model.fit(X_train, y_train)

# Modelin test verilerindeki başarısını hesaplayalım
basari = model.score(X_test, y_test)

print("Model başarı oranı:", basari)
print("Model başarı yüzdesi:", basari * 100)

# Yeni bir çiçeğin ölçülerini belirleyelim
# [Sepal length, Sepal width, Petal length, Petal width]
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]

# Yeni çiçeğin türünü tahmin edelim
tahmin = model.predict(yeni_cicek)

# Tahmin edilen çiçeğin adını bulalım
cicek_adi = iris.target_names[tahmin[0]]

print("Tahmin edilen çiçek türü:", cicek_adi)


# Yeni çiçeğin her sınıfa ait olma olasılığını hesaplayalım
olasiliklar = model.predict_proba(yeni_cicek)

# Çiçek türlerini ve olasılıklarını yazdıralım
for i in range(3):
    print(iris.target_names[i], ":", round(olasiliklar[0][i] * 100, 2), "%")
