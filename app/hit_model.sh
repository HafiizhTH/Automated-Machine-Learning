#!/bin/bash

# Menyimpan timestamp awal
echo "$(date) - Mulai menjalankan model.py" >> /var/log/cron.log

# Jalankan perintah Python dan simpan output ke logfile
python3 /model_automation/app/model.py >> /var/log/cron.log 2>&1

# Menyimpan timestamp akhir
echo "$(date) - Selesai menjalankan model.py" >> /var/log/cron.log