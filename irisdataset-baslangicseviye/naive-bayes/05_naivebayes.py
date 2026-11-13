
# UYGULAMA 4: Naive Bayes ile karışıklık matrisi

from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Veri setini yükleyelim
iris = load_iris()

X = iris.data
y = iris.target

# Verileri ayıralım
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Modeli eğitelim
model = GaussianNB()
model.fit(X_train, y_train)

# Tahmin yapalım
tahminler = model.predict(X_test)

# Karışıklık matrisini hesaplayalım
matris = confusion_matrix(y_test, tahminler)

print("Karışıklık Matrisi:")
print(matris)

# Matrisi grafik olarak gösterelim
gosterim = ConfusionMatrixDisplay(
    confusion_matrix=matris,
    display_labels=iris.target_names
)

gosterim.plot(cmap="Blues")

plt.title("Naive Bayes Karışıklık Matrisi")
plt.show()
