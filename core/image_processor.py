def crop_area(image, rect, scale):
    return image.crop((
        int(rect.x() * scale),
        int(rect.y() * scale),
        int((rect.x()+rect.width()) * scale),
        int((rect.y()+rect.height()) * scale)
    ))