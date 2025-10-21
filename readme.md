## thiết lập:

```
sudo apt install ffmpeg sox
python3 -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install numpy scipy librosa unidecode inflect tqdm matplotlib phonemizer pyyaml tensorboard
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
 │    └── metadata_val.csv
 ├── train.py
 └── inference.py
```