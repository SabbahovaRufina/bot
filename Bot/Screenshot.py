import pyautogui
from pytesseract import pytesseract
from PIL import Image, ImageEnhance
from typing import List
from config import HIGH, WIDTH
import re


class Screenshot:
    def __init__(self, path):
        self.path = path

    async def get_screenshot(self):
        pyautogui.screenshot(self.path)

    async def get_text_from_screenshot(self) -> List[str]:
        pytesseract.tesseract_cmd = r'C:\Users\Dima vse horosho\AppData\Local\Tesseract-OCR\tesseract.exe'
        with Image.open(self.path) as img:
            img = img.resize((WIDTH, HIGH))
            img = ImageEnhance.Contrast(img)
            img = img.enhance(2)
            text = pytesseract.image_to_string(img, lang='rus').split()
        return list(filter(lambda j: len(j) > 3, text))

    @staticmethod
    async def make_regular(*words: str) -> str:
        return '|'.join(words)

    @staticmethod
    async def is_reg_exp_in_words(words: List[str], regex: str) -> bool:
        for word in words:
            if re.search(regex, word):
                return True
        return False

    async def process_screenshot(self) -> bool:
        await self.get_screenshot()
        screenshot_words = await self.get_text_from_screenshot()
        regex = await self.make_regular('погиб', 'удар$')
        return await self.is_reg_exp_in_words(screenshot_words, regex)

