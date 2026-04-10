from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QRect, QPoint

HANDLE_SIZE = 8

class ImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.start = None
        self.end = None
        self.rectangles = []
        self.texts = []
        self.angles = []  # 🔥 NUEVO
        self.selected_index = -1
        self.drawing = False
        self.resizing = False
        self.resize_corner = None

    def get_handle(self, rect, pos):
        corners = {
            "tl": rect.topLeft(),
            "tr": rect.topRight(),
            "bl": rect.bottomLeft(),
            "br": rect.bottomRight()
        }
        for key, point in corners.items():
            area = QRect(point - QPoint(HANDLE_SIZE, HANDLE_SIZE), point + QPoint(HANDLE_SIZE, HANDLE_SIZE))
            if area.contains(pos):
                return key
        return None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            for i, rect in enumerate(self.rectangles):
                handle = self.get_handle(rect, event.pos())
                if handle:
                    self.selected_index = i
                    self.resizing = True
                    self.resize_corner = handle
                    return

                if rect.contains(event.pos()):
                    self.selected_index = i
                    self.window().update_editor()
                    self.update()
                    return

            self.start = event.pos()
            self.end = self.start
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.resizing and self.selected_index >= 0:
            rect = self.rectangles[self.selected_index]

            if self.resize_corner == "br":
                rect.setBottomRight(event.pos())
            elif self.resize_corner == "tr":
                rect.setTopRight(event.pos())
            elif self.resize_corner == "bl":
                rect.setBottomLeft(event.pos())
            elif self.resize_corner == "tl":
                rect.setTopLeft(event.pos())

            self.rectangles[self.selected_index] = rect.normalized()
            self.update()
            return

        if self.drawing:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if self.resizing:
            self.resizing = False
            return

        if self.drawing and self.start and self.end:
            rect = QRect(self.start, self.end).normalized()

            if rect.width() > 10 and rect.height() > 10:
                self.rectangles.append(rect)
                self.texts.append("")
                self.angles.append(0)  # 🔥 NUEVO
                self.selected_index = len(self.rectangles) - 1
                self.window().update_editor()

            self.start = None
            self.end = None
            self.drawing = False
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)

        for i, rect in enumerate(self.rectangles):
            pen = QPen(Qt.red if i == self.selected_index else Qt.blue, 2)
            painter.setPen(pen)

            painter.fillRect(rect, QColor(255, 255, 255, 115))
            painter.drawRect(rect)

            for point in [rect.topLeft(), rect.topRight(), rect.bottomLeft(), rect.bottomRight()]:
                painter.fillRect(QRect(point - QPoint(4,4), point + QPoint(4,4)), QColor(0,0,255))

            painter.setPen(Qt.black)
            painter.drawText(rect, Qt.AlignCenter | Qt.TextWordWrap, self.texts[i])