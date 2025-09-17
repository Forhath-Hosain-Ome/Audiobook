from gtts import gTTS
import os

def generate_tts_gtts(text: str, out_path: str, lang: str = "bn", slow: bool = False):

    tts = gTTS(text=text, lang=lang, slow=slow)
    # ensure dir exists
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    tts.save(out_path)
    return out_path
