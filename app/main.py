from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import uvicorn

app = FastAPI()

# Folder tujuan untuk menyimpan file yang diupload
UPLOAD_DIR = "/model_automation/data_mentah"

# Pastikan direktori tujuan ada
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Model Automation API"}

@app.post("/upload-file/")
async def upload_file(file: UploadFile = File(...)):
    # Memeriksa apakah file yang diupload adalah file CSV atau Excel
    if not (file.filename.endswith('.csv') or file.filename.endswith('.xlsx') or file.filename.endswith('.xls')):
        raise HTTPException(status_code=400, detail="File yang diupload bukan file CSV/Excel")

    # Tentukan jalur lengkap untuk menyimpan file
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Periksa apakah file sudah ada
    if os.path.exists(file_path):
        return {"filename": file.filename, "status": "File sudah ada"}

    # Simpan file ke direktori tujuan
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"filename": file.filename, "status": "File berhasil diupload"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
