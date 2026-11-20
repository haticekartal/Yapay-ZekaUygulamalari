# Yapay Zekâ Uygulamaları

Python ile yapay zekâya giriş için hazırlanmış, başlangıç seviyesine uygun örnek kodlar.

Örnekler NumPy ve Matplotlib temelleriyle başlar; Scikit-learn kullanarak KNN, Karar Ağacı, Naive Bayes ve SVM ile sınıflandırmaya kadar ilerler. Kodların tamamında Türkçe açıklama satırları bulunur.

> **Önce kurulum:** Kodların çalışması için gerekli kütüphanelerin kurulu olması gerekir. Aşağıdaki [Kütüphane kurulumu](#kütüphane-kurulumu) bölümünü tamamlamadan örneklere geçmeyin.

## Kütüphane kurulumu

Örnekleri çalıştırmadan önce aşağıdaki adımları sırayla tamamlayın. Kurulum bir kez yapılır.

### 1. Python'un kurulu olduğunu kontrol edin

Terminali (Windows'ta Komut İstemi ya da PowerShell) açın ve şunu yazın:

```bash
python --version
```

Sürüm numarası görünüyorsa Python kuruludur. Komut tanınmıyorsa Windows'ta `py --version`, macOS ve Linux'ta `python3 --version` deneyin. Hiçbiri çalışmıyorsa Python'u [python.org](https://www.python.org/downloads/) adresinden kurun; Windows kurulumunda **"Add Python to PATH"** kutusunu işaretleyin.

> Aşağıdaki komutlarda `python` yazan yerlerde, sizde çalışan komutu (`py` ya da `python3`) kullanın.

### 2. Kütüphaneleri kurun

Tüm kütüphaneleri tek komutla kurabilirsiniz:

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn openpyxl
```

Tek tek kurmak isterseniz:

```bash
python -m pip install numpy
python -m pip install pandas
python -m pip install matplotlib
python -m pip install seaborn
python -m pip install scikit-learn
python -m pip install openpyxl
```

| Kütüphane | Kurulum adı | Kodda yazılışı | Ne için kullanılır? | Hangi klasörlerde? |
|---|---|---|---|---|
| NumPy | `numpy` | `import numpy as np` | Sayısal diziler | `numpy/`, Iris örnekleri |
| Pandas | `pandas` | `import pandas as pd` | Tablolar ve Excel dosyaları | `numpy/`, Iris örnekleri |
| Matplotlib | `matplotlib` | `import matplotlib.pyplot as plt` | Grafik çizimi | `matplotlib/`, Iris örnekleri |
| Seaborn | `seaborn` | `import seaborn as sns` | Gelişmiş grafikler | `irisdataset-ileriseviye/` |
| Scikit-learn | `scikit-learn` | `from sklearn...` | Algoritmalar ve veri setleri | `knn-ornekleri/`, Iris örnekleri |
| openpyxl | `openpyxl` | Doğrudan yazılmaz | Pandas'ın Excel okuyup yazması | `numpy/` |

**Dikkat:** Scikit-learn `scikit-learn` adıyla kurulur, ama kodda `sklearn` olarak yazılır. `pip install sklearn` komutu doğru değildir.

### 3. Kurulumu doğrulayın

Aşağıdaki kodu `kontrol.py` adıyla kaydedip çalıştırın:

```python
import numpy, pandas, matplotlib, seaborn, sklearn, openpyxl

print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Seaborn:", seaborn.__version__)
print("Scikit-learn:", sklearn.__version__)
print("openpyxl:", openpyxl.__version__)
print("Tüm kütüphaneler kurulu.")
```

Sürüm numaraları ve son satır görünüyorsa kurulum tamamdır. Hata alırsanız hata mesajında adı geçen kütüphaneyi 2. adımdaki komutla yeniden kurun.

### 4. VS Code ve Jupyter kullananlar için

- **VS Code:** Kütüphaneleri kurduğunuz Python'un seçili olduğundan emin olun. `Ctrl + Shift + P` tuşlarına basın, **Python: Select Interpreter** yazın ve kurulum yaptığınız Python'u seçin.
- **Jupyter:** Kütüphaneleri defterin içinden kurmak için bir hücreye şunu yazıp çalıştırın:

  ```python
  %pip install numpy pandas matplotlib seaborn scikit-learn openpyxl
  ```

  Jupyter'in kendisi kurulu değilse: `python -m pip install notebook`

### 5. İsteğe bağlı: Sanal ortam

Kütüphaneleri bu projeye özel bir ortama kurmak isterseniz, depo klasöründe:

```bash
python -m venv .venv
```

Ortamı etkinleştirin:

```bash
# Windows
.venv\Scripts\activate

# macOS ve Linux
source .venv/bin/activate
```

Ardından 2. adımdaki kurulum komutunu çalıştırın.

### Sık karşılaşılan kurulum hataları

| Hata mesajı | Nedeni | Çözümü |
|---|---|---|
| `ModuleNotFoundError: No module named 'sklearn'` | Scikit-learn kurulu değil | `python -m pip install scikit-learn` |
| `ModuleNotFoundError: No module named 'numpy'` (ya da başka bir ad) | Adı geçen kütüphane kurulu değil | `python -m pip install` ve kütüphanenin kurulum adı |
| `Missing optional dependency 'openpyxl'` | Excel desteği kurulu değil | `python -m pip install openpyxl` |
| `'pip' is not recognized` ya da `pip: command not found` | `pip` komutu yolda tanımlı değil | `pip` yerine `python -m pip` yazın |
| Kurdum ama hâlâ `ModuleNotFoundError` alıyorum | Kütüphane başka bir Python'a kurulmuş | `python -m pip` ile kurun; VS Code'da doğru Python'u seçin |
| `externally-managed-environment` | Sistem Python'una kurulum kısıtlı (macOS, Linux) | 5. adımdaki sanal ortamı kullanın |

## Depoyu indirme

```bash
git clone https://github.com/haticekartal/Yapay-ZekaUygulamalari.git
cd Yapay-ZekaUygulamalari
```

Git kullanmıyorsanız GitHub sayfasındaki **Code → Download ZIP** ile de indirebilirsiniz.

## İçindekiler

| Klasör | Konu | Neler var? |
|---|---|---|
| [`numpy/`](numpy) | NumPy ve Pandas | Dizi işlemleri, Excel dosyası oluşturma ve okuma |
| [`matplotlib/`](matplotlib) | Grafik çizimi | Çizgi, sütun, yatay sütun, pasta ve karşılaştırma grafikleri |
| [`knn-ornekleri/`](knn-ornekleri) | KNN algoritması | Meyve ve renk sınıflandırma örnekleri |
| [`irisdataset-baslangicseviye/`](irisdataset-baslangicseviye) | Iris ile sınıflandırma | Veri setini tanıma, KNN, Karar Ağacı, Naive Bayes, SVM |
| [`irisdataset-ileriseviye/`](irisdataset-ileriseviye) | Iris: ayrıntılı çalışma | Başarı metrikleri, görselleştirme, ilk model, Jupyter defteri |

## Önerilen çalışma sırası

1. **`numpy/`**: Dizilerle ve tablolarla çalışmayı öğrenin.
2. **`matplotlib/`**: Verileri grafiğe dökün.
3. **`knn-ornekleri/`**: İlk sınıflandırma algoritmanızı küçük verilerle deneyin.
4. **`irisdataset-baslangicseviye/`**: Dört farklı algoritmayı aynı veri seti üzerinde karşılaştırın.
5. **`irisdataset-ileriseviye/`**: Metrikleri, görselleştirmeyi ve model değerlendirmeyi derinleştirin.

## Çalıştırma

Çalıştırmak istediğiniz örneğin klasörüne girin ve dosyayı Python ile çalıştırın:

```bash
cd knn-ornekleri
python 01_knn_ornegi.py
```

Dikkat edilecek noktalar:

- Excel örnekleri dosyaları bulundukları klasörde arar. Bu yüzden komutu `numpy/` klasörünün içinde çalıştırın.
- Bazı örnekler klavyeden değer girmenizi ister (örneğin çiçek ölçüleri).
- Grafik çizen örnekler ayrı bir pencere açar; program, pencere kapatılınca devam eder.

Jupyter defterini açmak için:

```bash
jupyter notebook irisdataset-ileriseviye/Iris_Ders_Kodlari.ipynb
```

## Klasör ayrıntıları

### `numpy/`

| Dosya | Açıklama |
|---|---|
| `dizi_olusturma.py` | Dizi oluşturma, dört işlem, en büyük değeri bulma gibi temel NumPy işlemleri |
| `excelolusturma.py` | Öğrenci notlarından tablo oluşturur ve `ogrenci_notlari.xlsx` dosyasına kaydeder |
| `excelolusturma2.py` | Aylık gider tablosu oluşturur ve `aylik_giderler.xlsx` dosyasına kaydeder |
| `exceltablosu2_islemler.py` | Giderlerin toplamını ve ortalamasını hesaplayıp Excel dosyasına yazar |
| `exceldosya_okuma.py` | Excel dosyasındaki notları okur ve NumPy dizisine dönüştürür |

### `matplotlib/`

| Dosya | Açıklama |
|---|---|
| `grafik1.py` | Çizgi grafiğini adım adım geliştirme: başlık, eksen adları ve diğer ayarlar |
| `sutungrafik1.py` | Öğrenci notlarıyla sütun grafiği |
| `yataysutungrafigi2.py` | Ürün satışlarıyla yatay sütun grafiği |
| `pastagrafik3.py` | Ders çalışma süreleriyle pasta grafiği |
| `cizgigrafik4.py` | Günlük satışlarla işaretli ve kesikli çizgi grafiği |
| `karsilastirmagrafik.py` | İki ürünün satışlarını aynı grafikte karşılaştırma |

### `knn-ornekleri/`

| Dosya | Açıklama |
|---|---|
| `01_knn_ornegi.py` | Kütüphane kullanmadan KNN: uzaklık hesabıyla meyve sınıflandırma |
| `02_knn_ornegi.py` | Scikit-learn ile meyve sınıflandırma |
| `03_knn_ornegi.py` | Parlaklık ve doygunluk değerleriyle renk sınıflandırma |
| `04_knn_ornegi.py` | Kullanıcının girdiği değerlere göre renk tahmini |

### `irisdataset-baslangicseviye/`

| Alt klasör | Açıklama |
|---|---|
| `iris-veri-seti/` | Veri setini tanıma, tabloya dönüştürme, çiçek türleri, Matplotlib grafikleri ve diğer hazır veri setleri |
| `knn-algoritmasi/` | KNN'i elle yazma, Scikit-learn ile KNN, doğruluk hesabı ve K değerine göre başarı grafiği |
| `karar-agaci-algoritmasi/` | Karar ağacı eğitimi, kullanıcı girdisiyle tahmin, ağacın çizimi ve KNN ile karşılaştırma |
| `naive-bayes/` | Naive Bayes ile tahmin, doğruluk, karışıklık matrisi ve üç algoritmanın karşılaştırması |
| `svm/` | SVM ile sınıflandırma, doğruluk, kullanıcı girdisiyle tahmin ve kernel türlerinin karşılaştırması |

### `irisdataset-ileriseviye/`

| Dosya | Açıklama |
|---|---|
| `01_siniflandirma_ornegi.py` | Spam e-posta örneğiyle sınıflandırmanın eğitim ve tahmin aşamaları |
| `02_basari_metrikleri.py` | Doğruluk, kesinlik, duyarlılık ve F1 skorunun hesaplanması |
| `03_iris_yukleme_ve_inceleme.py` | Iris veri setini Scikit-learn ve Pandas ile yükleme ve inceleme |
| `04_gorsellestirme.py` | Matplotlib ve Seaborn ile Iris veri setinin görselleştirilmesi |
| `05_siniflandirma_modeli.py` | Karar ağacı ile ilk sınıflandırma modeli |
| `ek_kavramsal_sekiller.py` | Ders dokümanındaki kavramsal şekilleri üreten kod |
| `Iris_Ders_Kodlari.ipynb` | Ders kodlarının tamamını içeren Jupyter defteri |
| `requirements.txt` | Bu klasör için gerekli kütüphaneler |

Bu klasörün kütüphanelerini `requirements.txt` ile de kurabilirsiniz:

```bash
python -m pip install -r irisdataset-ileriseviye/requirements.txt
```

## Kullanılan veri setleri

- **Iris:** 150 çiçeğin dört ölçümünü ve üç türünü içeren klasik veri seti. Scikit-learn ile birlikte gelir; ayrıca indirmeniz gerekmez.
- **Wine ve Breast Cancer:** Scikit-learn'deki diğer hazır veri setlerini tanıtan örnekte kullanılır.
- **Diğer veriler:** KNN örneklerindeki meyve ve renk verileri ile Excel tablolarındaki notlar ve giderler, öğretim amacıyla hazırlanmış küçük örnek verilerdir.

## Katkı ve geri bildirim

Bir hata fark ederseniz ya da öneriniz varsa [Issues](https://github.com/haticekartal/Yapay-ZekaUygulamalari/issues) bölümünden bildirebilirsiniz.
