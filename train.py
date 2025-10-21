import torch
import torch.optim as optim
from tqdm import tqdm
import os, json
from vits.model import VITS
from vits.dataset import TTSDataset

# Load config
with open("data/configs/config_vi.json") as f:
    config = json.load(f)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset & loader
dataset = TTSDataset(config["data"])
dataloader = torch.utils.data.DataLoader(
    dataset, batch_size=config["train"]["batch_size"], shuffle=True
)

# Model
model = VITS(config["model"]).to(device)
optimizer = optim.Adam(
    model.parameters(),
    lr=config["train"]["learning_rate"],
    betas=tuple(config["train"]["betas"]),
    eps=config["train"]["eps"]
)
scheduler = torch.optim.lr_scheduler.ExponentialLR(
    optimizer, gamma=config["train"]["lr_decay"]
)

os.makedirs("logs", exist_ok=True)

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
    
    scheduler.step()

    if (epoch + 1) % config["train"]["save_every_epoch"] == 0:
        torch.save(model.state_dict(), f"logs/vits_voice_clone_{epoch+1}.pth")

torch.save(model.state_dict(), "logs/vits_voice_clone.pth")
print("✅ Training done.")
