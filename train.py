import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import os, json, librosa, soundfile as sf
from vits.model import VITS
from vits.dataset import TTSDataset

# Load config
with open("configs/config.json") as f:
    config = json.load(f)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load dataset
dataset = TTSDataset(config["data"])
dataloader = torch.utils.data.DataLoader(dataset, batch_size=config["train"]["batch_size"], shuffle=True)

# Create model
model = VITS(config["model"]).to(device)
optimizer = optim.Adam(model.parameters(), lr=config["train"]["learning_rate"])

# Training loop
for epoch in range(config["train"]["epochs"]):
    loop = tqdm(dataloader, desc=f"Epoch {epoch+1}")
    for mel, text, wav in loop:
        mel, text, wav = mel.to(device), text.to(device), wav.to(device)
        loss = model.loss(mel, text, wav)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loop.set_postfix(loss=loss.item())
    
    if (epoch + 1) % 10 == 0:
        torch.save(model.state_dict(), f"logs/vits_voice_clone_{epoch+1}.pth")

# Save final
torch.save(model.state_dict(), "logs/vits_voice_clone.pth")
print("✅ Training done. Model saved to logs/vits_voice_clone.pth")
