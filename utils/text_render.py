from PIL import ImageFont

def draw_text_box(draw, text, box):
    if not text or text.strip() == "":
        return  # 🔥 evita dibujar vacío

    x1, y1, x2, y2 = box
    width = x2 - x1
    height = y2 - y1

    font_size = min(height, width)

    while font_size > 8:
        try:
            font = ImageFont.truetype("comic.ttf", font_size)
        except:
            font = ImageFont.load_default()

        words = text.split()
        lines = []
        line = ""

        valid = True

        for word in words:
            test = (line + " " + word).strip()

            if draw.textlength(test, font=font) <= width:
                line = test
            else:
                if line == "":
                    # 🔥 palabra demasiado larga → reducir font
                    valid = False
                    break
                lines.append(line)
                line = word

        if not valid:
            font_size -= 2
            continue

        if line:
            lines.append(line)

        # 🔥 validación final
        if not lines:
            font_size -= 2
            continue

        too_wide = any(draw.textlength(l, font=font) > width for l in lines)
        total_height = len(lines) * (font_size + 4)

        if not too_wide and total_height <= height:
            break

        font_size -= 2

    # 🔥 fallback extremo (nunca queda vacío)
    if not lines:
        lines = [text]

    # ===== centrado =====
    total_height = len(lines) * (font_size + 4)
    y_text = y1 + (height - total_height) // 2

    for line in lines:
        if not line.strip():
            continue

        line_width = draw.textlength(line, font=font)
        x_text = x1 + (width - line_width) // 2

        draw.text((x_text, y_text), line, fill=(0, 0, 0), font=font)
        y_text += font_size + 4