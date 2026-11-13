
# UYGULAMA 3: Naive Bayes modelinin başarısını hesaplama

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Eğitim ve test verilerini ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Modeli oluşturalım
model = GaussianNB()

# Modeli eğitelim
model.fit(X_train, y_train)

# Test verilerinin sınıflarını tahmin edelim
tahminler = model.predict(X_test)

# Başarı oranını hesaplayalım
basari = accuracy_score(y_test, tahminler)

print("Model başarı oranı:", basari)
print("Model başarı yüzdesi:", basari * 100)
