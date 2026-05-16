import docx
import os
from pathlib import Path

# 상대 경로 설정 (공유용)
BASE_DIR = Path(__file__).parent
docx_path = BASE_DIR / "06_Output" / "final.docx"

def convert():
    print("Converting DOCX to MD...")
    # Clean logic
