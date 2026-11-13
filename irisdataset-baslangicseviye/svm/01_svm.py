
# UYGULAMA 1: Iris veri setiyle SVM sınıflandırması

from sklearn.datasets import load_iris
from sklearn.svm import SVC

# Iris veri setini yükleyelim
iris = load_iris()

# Çiçeklerin özelliklerini ve türlerini ayıralım
X = iris.data
y = iris.target

# SVM modelini oluşturalım
model = SVC(kernel="linear")

# Modeli eğitelim
model.fit(X, y)

# Yeni çiçeğin ölçülerini belirleyelim
yeni_cicek = [[5.1, 3.5, 1.4, 0.2]]

# Tahmin yapalım
tahmin = model.predict(yeni_cicek)

# Tahmin edilen çiçeğin adını bulalım
cicek_adi = iris.target_names[tahmin[0]]

print("Tahmin edilen çiçek türü:", cicek_adi)
