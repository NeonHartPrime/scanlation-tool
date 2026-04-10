from PyQt5.QtWidgets import (
    QMainWindow, QFileDialog, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QTextEdit,
    QScrollArea, QFrame
)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap, QImage  # 🔥 IMPORTANTE (para evitar crashes)
from datetime import datetime

from ui.image_label import ImageLabel
from core.translator import translate_image
from core.image_processor import crop_area
from utils.text_render import draw_text_box


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scanlation Tool PRO")

        # ===== WIDGETS =====
        self.image_label = ImageLabel(self)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.image_label)

        self.text_editor = QTextEdit()
        self.text_editor.setPlaceholderText("Editar texto seleccionado...")
        self.text_editor.textChanged.connect(self.update_text)

        load_btn = QPushButton("Cargar Imagen")
        translate_btn = QPushButton("Traducir")
        export_btn = QPushButton("Exportar")

        load_btn.clicked.connect(self.load_image)
        translate_btn.clicked.connect(self.translate_all)
        export_btn.clicked.connect(self.export_image)

        # ===== PANEL IZQUIERDO =====
        left_panel = QVBoxLayout()
        left_panel.addWidget(load_btn)
        left_panel.addWidget(translate_btn)
        left_panel.addWidget(export_btn)
        left_panel.addStretch()
        left_panel.addWidget(self.text_editor)

        left_container = QWidget()
        left_container.setLayout(left_panel)
        left_container.setFixedWidth(260)

        # ===== SEPARADOR =====
        separator = QFrame()
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Sunken)

        # ===== LAYOUT PRINCIPAL =====
        main_layout = QHBoxLayout()
        main_layout.addWidget(left_container)
        main_layout.addWidget(separator)
        main_layout.addWidget(self.scroll)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # ===== ESTILO BASE =====
        self.setStyleSheet("""
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
            font-size: 13px;
        }

        QPushButton {
            background-color: #3c3f41;
            border: none;
            padding: 8px;
            border-radius: 4px;
        }

        QPushButton:hover {
            background-color: #505354;
        }

        QTextEdit {
            background-color: #1e1e1e;
            border: 1px solid #555;
        }

        QScrollArea {
            border: none;
        }
        """)

        self.image = None

    # =============================
    def load_image(self):
        path, _ = QFileDialog.getOpenFileName()
        if path:
            try:
                self.image = Image.open(path)
                self.image = self.image.convert("RGB")

                preview = self.image.copy()
                preview.thumbnail((1000, 10000))

                # 🔥 Conversión segura sin ImageQt
                data = preview.tobytes("raw", "RGB")
                qimg = QImage(
                    data,
                    preview.width,
                    preview.height,
                    preview.width * 3,  # 🔥 FIX CRÍTICO (stride correcto)
                    QImage.Format_RGB888
                )

                pixmap = QPixmap.fromImage(qimg)

                self.image_label.setPixmap(pixmap)
                self.image_label.resize(pixmap.width(), pixmap.height())

                self.image_label.rectangles = []
                self.image_label.texts = []

            except Exception as e:
                print("Error cargando imagen:", e)

    # =============================
    def update_editor(self):
        i = self.image_label.selected_index
        if i >= 0:
            self.text_editor.blockSignals(True)
            self.text_editor.setPlainText(self.image_label.texts[i])
            self.text_editor.blockSignals(False)

    # =============================
    def update_text(self):
        i = self.image_label.selected_index
        if i >= 0:
            self.image_label.texts[i] = self.text_editor.toPlainText()
            self.image_label.update()

    # =============================
    def translate_all(self):
        if not self.image:
            return

        for i, rect in enumerate(self.image_label.rectangles):
            if self.image_label.texts[i].strip():
                continue

            try:
                scale = self.image.width / self.image_label.pixmap().width()
                crop = crop_area(self.image, rect, scale)
                text = translate_image(crop)
                self.image_label.texts[i] = text

            except Exception as e:
                print("Error:", e)
                self.image_label.texts[i] = "[ERROR]"

            self.image_label.update()

    # =============================
    def export_image(self):
        if not self.image:
            return

        output = self.image.copy()
        draw = ImageDraw.Draw(output)

        for i, rect in enumerate(self.image_label.rectangles):
            scale = self.image.width / self.image_label.pixmap().width()

            x1 = int(rect.x() * scale)
            y1 = int(rect.y() * scale)
            x2 = int((rect.x()+rect.width()) * scale)
            y2 = int((rect.y()+rect.height()) * scale)

            draw.rectangle([x1, y1, x2, y2], fill=(255, 255, 255))
            draw_text_box(draw, self.image_label.texts[i], (x1, y1, x2, y2))

        timestamp = datetime.now().strftime("%H_%M_%S")
        filename = f"resultado_{timestamp}.png"

        output.save(filename)
        print(f"Imagen guardada como {filename}")