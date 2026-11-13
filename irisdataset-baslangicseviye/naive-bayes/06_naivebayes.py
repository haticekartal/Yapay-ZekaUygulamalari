
# UYGULAMA 5: Üç farklı algoritmanın karşılaştırılması

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Iris veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Verileri eğitim ve test olarak ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 1. Naive Bayes
naive_bayes = GaussianNB()
naive_bayes.fit(X_train, y_train)

# 2. KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 3. Karar Ağacı
karar_agaci = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
karar_agaci.fit(X_train, y_train)

# Başarı oranlarını hesaplayalım
basari_nb = naive_bayes.score(X_test, y_test)
basari_knn = knn.score(X_test, y_test)
basari_dt = karar_agaci.score(X_test, y_test)

print("Naive Bayes başarısı:", round(basari_nb * 100, 2), "%")
print("KNN başarısı:", round(basari_knn * 100, 2), "%")
print("Karar Ağacı başarısı:", round(basari_dt * 100, 2), "%")
