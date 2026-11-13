
# UYGULAMA 3: Kullanıcıdan ölçü alarak SVM tahmini

from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris = load_iris()

X = iris.data
y = iris.target

# Modeli oluşturalım ve eğitelim
model = SVC(kernel="linear")
model.fit(X, y)

# Kullanıcıdan çiçek ölçülerini alalım
sepal_uzunluk = float(input("Sepal uzunluğu: "))
sepal_genislik = float(input("Sepal genişliği: "))
petal_uzunluk = float(input("Petal uzunluğu: "))
petal_genislik = float(input("Petal genişliği: "))

# Ölçüleri modele uygun listeye dönüştürelim
yeni_cicek = [[
    sepal_uzunluk,
    sepal_genislik,
    petal_uzunluk,
    petal_genislik
]]

# Tahmin yapalım
tahmin = model.predict(yeni_cicek)

print("Tahmin edilen tür:", iris.target_names[tahmin[0]])
