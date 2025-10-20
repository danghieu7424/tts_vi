import re

def bilingual_cleaners(text):
    # Giữ nguyên hoa-thường, không xóa tag
    # Giữ ký tự tiếng Việt, tiếng Anh, và các dấu ngoặc vuông/tròn
    text = re.sub(r"[^a-zA-ZÀ-Ỹà-ỹ0-9\s,\.!?\'\"\-\[\]\(\)]", "", text)
    
    # Tách tag [vi](text) hoặc [en](text) thành dạng dễ đọc cho model
    # Ví dụ: [vi](xin chào) -> <vi> xin chào </vi>
    text = re.sub(r"\[vi\]\((.*?)\)", r"<vi> \1 </vi>", text)
    text = re.sub(r"\[en\]\((.*?)\)", r"<en> \1 </en>", text)

    return text.strip()
