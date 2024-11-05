import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
warnings.filterwarnings('ignore')

# Path folder data mentah dan data hasil training
data_mentah_folder = r"/model_automation/data_mentah"
data_training_folder = r"/model_automation/data_training"

# Fungsi untuk memuat dataset
def load_dataset(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path)
    else:
        return None

# Mendapatkan daftar file dataset dalam folder data_mentah
datasets = [os.path.join(data_mentah_folder, f) for f in os.listdir(data_mentah_folder) if f.endswith(('.csv', '.xlsx', '.xls'))]

# Cek jika folder data_mentah kosong
if not datasets:
    print("Tidak ada data yang harus diproses.")
else:
    # Loop melalui setiap dataset
    for dataset_path in datasets:
        # Memuat dataset
        data = load_dataset(dataset_path)
        if data is None:
            continue

        # Memisahkan fitur (X) dan target (y)
        X = data.drop(columns=['Risk_Class'])
        y = data['Risk_Class']

        # Memisahkan data menjadi data latih dan data uji
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Daftar model yang akan diuji
        models = {
            'Decision Tree': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier()
        }

        # Inisialisasi dictionary untuk menyimpan metrik evaluasi
        accuracy, precision, recall, f1, roc_auc, cross_val = {}, {}, {}, {}, {}, {}

        # Variabel untuk menyimpan model terbaik
        best_model_name = None
        best_model_score = -np.inf

        # Loop melalui setiap model untuk training dan evaluasi
        for name, model in models.items():
            # Melatih model
            model.fit(X_train, y_train)

            # Melakukan prediksi pada data uji
            predict = model.predict(X_test)

            # Menghitung metrik evaluasi
            accuracy[name] = accuracy_score(y_test, predict)
            precision[name] = precision_score(y_test, predict)
            recall[name] = recall_score(y_test, predict)
            f1[name] = f1_score(y_test, predict)
            roc_auc[name] = roc_auc_score(y_test, predict)

            # Menghitung nilai cross-validation
            cross_val[name] = np.mean(cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy'))

            # Menghitung rata-rata skor dari semua metrik
            avg_score = np.mean([accuracy[name], precision[name], recall[name], f1[name], roc_auc[name], cross_val[name]])

            # Memperbarui model terbaik jika skor rata-rata lebih tinggi
            if avg_score > best_model_score:
                best_model_score = avg_score
                best_model_name = name

        # Menampilkan hasil evaluasi untuk setiap model
        df_model = pd.DataFrame(index=models.keys(), columns=['Accuracy', 'Precision', 'Recall', 'F1-Score', 'Roc_Auc', 'Cross_Val'])
        df_model['Accuracy'] = accuracy.values()
        df_model['Precision'] = precision.values()
        df_model['Recall'] = recall.values()
        df_model['F1-Score'] = f1.values()
        df_model['Roc_Auc'] = roc_auc.values()
        df_model['Cross_Val'] = cross_val.values()

        print(f"\nHasil untuk dataset: {os.path.basename(dataset_path)}")
        print(round(df_model, 2))
        print(f"\nModel Terbaik: {best_model_name} dengan rata-rata skor: {round(best_model_score, 2)}")

        # Menyimpan model terbaik jika skor rata-rata di atas 80%
        if best_model_score > 0.8:
            best_model = models[best_model_name]
            model_filename = os.path.splitext(os.path.basename(dataset_path))[0] + '.pkl'
            model_path = os.path.join(data_training_folder, model_filename)
            with open(model_path, 'wb') as file:
                pickle.dump(best_model, file)
            print(f"Model disimpan: {model_path}")
        else:
            print(f"Model tidak disimpan, karena skor model terbaik di bawah 80%: {round(best_model_score, 2)}")

        # Menghapus dataset yang telah diproses, cek terlebih dahulu jika file masih ada
        if os.path.exists(dataset_path):
            os.remove(dataset_path)
            print(f"Dataset dihapus: {dataset_path}")
        else:
            print(f"Dataset {dataset_path} tidak ditemukan atau sudah dihapus sebelumnya.")
