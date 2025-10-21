import re

def bilingual_cleaners(text):
    # Giữ nguyên hoa-thường, ký tự tiếng Việt, Anh, và các dấu cơ bản
    text = re.sub(r"[^a-zA-ZÀ-Ỹà-ỹ0-9\s,\.!?\'\"\-\[\]\(\)]", "", text)

    # Xử lý tag [vi] và [en]
    text = re.sub(r"\[vi\]\((.*?)\)", r"<vi> \1 </vi>", text)
    text = re.sub(r"\[en\]\((.*?)\)", r"<en> \1 </en>", text)

    # Tách và bao các phần không có tag bằng <vi> ... </vi>
    parts = re.split(r"(\<en>.*?\<\/en>)", text)
    cleaned = ""
    for part in parts:
        if part.strip() == "":
            continue
        if part.startswith("<en>"):
            cleaned += part.strip() + " "
        else:
            cleaned += f"<vi> {part.strip()} </vi> "
    
    return cleaned.strip()
