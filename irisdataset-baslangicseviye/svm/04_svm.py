
# UYGULAMA 5: SVM kernel türlerini karşılaştırma

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

iris = load_iris()

X = iris.data
y = iris.target

# Eğitim ve test verilerini ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Kullanacağımız kernel türleri
kernel_turleri = ["linear", "rbf", "poly"]

# Her kernel için ayrı model oluşturalım
for kernel in kernel_turleri:

    # Ölçeklendirme ve SVM modelini birlikte kullanalım
    model = make_pipeline(
        StandardScaler(),
        SVC(kernel=kernel)
    )

    # Modeli eğitelim
    model.fit(X_train, y_train)

    # Test başarısını hesaplayalım
    basari = model.score(X_test, y_test)

    print(kernel, "başarı oranı:", round(basari * 100, 2), "%")
