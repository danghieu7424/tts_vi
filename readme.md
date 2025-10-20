```
py -3.10 -m venv venv
venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install setuptools wheel -U
```
```
#gpu
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
```
#cpu
pip install torch torchvision torchaudio
```
```
pip install -r requirements.txt
```

## 📁 Cấu trúc thư mục
```
vits_tts/
 ├── data/
 │    ├── configs/
 │    │    └── config_vi.json
 │    ├──  wavs/
 │    │    ├── 0
 │    │    │   ├── 0.wav
 │    │    │   ├── 1.wav
 │    │    │   └── ...
 │    │    ├── 1
 │    │    │   ├── 0.wav
 │    │    │   ├── 1.wav
 │    │    │   └── ...
 │    │    └── ...
 │    ├── metadata_1.csv
 │    ├── metadata_2.csv
 │    ├── metadata_3.csv
 │    └── metadata_test.csv
 ├── train.py
 └── inference.py
```