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
 │    ├── filelists/
 │    │    ├── sentences.txt
 │    │    ├── sentences_advanced.txt
 │    │    └── sentences_dialogue.txt
 │    └── wavs/
 │         ├── 0001.wav
 │         ├── 0002.wav
 │         └── ...
 ├── train.py
 └── inference.py
```