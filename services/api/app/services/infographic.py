from pathlib import Path

from PIL import Image, ImageDraw


class InfographicService:
    OUTPUT_DIR = Path('/tmp/finintel-infographics')

    @classmethod
    def render(cls, image_id: str, headline: str, summary: str, symbol: str) -> str:
        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = cls.OUTPUT_DIR / f'{image_id}.png'

        img = Image.new('RGB', (1080, 1080), color=(11, 18, 32))
        draw = ImageDraw.Draw(img)

        draw.rectangle((40, 40, 1040, 220), fill=(26, 46, 89))
        draw.text((70, 85), 'FinIntel Flash', fill=(255, 255, 255))
        draw.text((70, 150), f'Symbol: {symbol}', fill=(153, 234, 255))

        draw.text((70, 280), headline[:160], fill=(255, 255, 255))
        draw.text((70, 420), summary[:380], fill=(222, 222, 222))

        draw.rectangle((40, 900, 1040, 1020), fill=(18, 28, 44))
        draw.text((70, 945), 't.me/FinIntelBot', fill=(175, 214, 255))

        img.save(output_path)
        return str(output_path)
