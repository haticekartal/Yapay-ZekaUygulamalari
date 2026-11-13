
# UYGULAMA 2: SVM modelinin başarı oranını hesaplama

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Verileri %80 eğitim, %20 test olarak ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# SVM modelini oluşturalım
model = SVC(kernel="linear")

# Modeli eğitelim
model.fit(X_train, y_train)

# Test verilerini tahmin edelim
tahminler = model.predict(X_test)

# Accuracy değerini hesaplayalım
basari = accuracy_score(y_test, tahminler)

print("Model başarı oranı:", basari)
print("Model başarı yüzdesi:", basari * 100)
