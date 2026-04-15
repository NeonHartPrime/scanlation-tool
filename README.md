# 🖼️ Scanlation Tool PRO

Herramienta local para scanlation que permite seleccionar áreas de texto en imágenes, traducirlas con IA local y reinsertarlas automáticamente.

> 🔒 Funciona completamente offline usando IA local (LM Studio)

---

## 🖼️ Vista previa

<p align="center">
  <img src="assets/preview.png" width="750"/>
</p>

<p align="center">
  <img src="assets/preview2.png" width="750"/>
</p>

<p align="center">
  <img src="assets/example.png" width="750"/>
</p>

---

## 🚀 Características

* 📂 Soporte para imágenes largas (manhwa/webtoon)
* ✂️ Selección manual de múltiples áreas
* 🧠 OCR (extracción de texto) por lote o por selección individual
* 🔁 Re-OCR por cuadro para corregir errores fácilmente
* 📝 Edición manual del texto con sincronización en tiempo real
* 🔤 Sistema de **fuentes dinámicas** (soporte `.ttf` / `.otf`)
* 🎨 Renderizado de texto con **stroke y auto-ajuste inteligente**
* 🧩 Preview visual en tiempo real (WYSIWYG)
* ⚡ Sistema optimizado con **cache de renderizado** (sin lag)
* 🗑️ Eliminación de selecciones con tecla `Delete`
* 📤 Exportación final con fondo semitransparente y estilo profesional
* 🧩 Código modular y escalable (fácil de extender)

---

## ⚙️ Cómo funciona

1. Cargar imagen
2. Seleccionar áreas de texto
3. Presionar **Extraer texto (OCR)**
4. (Opcional) Re-extraer texto en áreas específicas
5. Editar texto y ajustar fuente si es necesario
6. Exportar imagen final

---

## 🆕 Novedades recientes

* ⚡ Mejora masiva de rendimiento en el preview
* 🔤 Selector de fuentes por cuadro de texto
* 🔁 Re-OCR individual sin reprocesar toda la imagen
* 🎨 Renderizado más profesional (stroke + fondo optimizado)
* 🧠 Sistema de cache para evitar render innecesario

---

## 🛠️ Tecnologías

- Python 3
- PyQt5
- Pillow
- LM Studio (IA local)

---

## 📦 Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/NeonHartPrime/scanlation-tool.git
cd scanlation-tool
```

### 2. Crear entorno virtual "Opcional"
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### ▶️ Uso
```bash
python main.py
```

### 🤖 Configuración IA (LM Studio)
* Asegúrate de tener LM Studio corriendo, verifica en:
```bash
 http://localhost:1234
```
* inicia el sv manualmente en cmd con:
```bash
lms server start
```
* Modelo Probado:
```bash
gemma-3-4b
qwen2vl
```
⚠️ Debe ser una versión compatible con imágenes

### 🎨 Personalización
* Para cambiar la fuente ve a "text_render.py" cambia "comic.ttf" por tu fuente. "no es necesario en nuevas verciones"
```bash
  font = ImageFont.truetype("comic.ttf", font_size)
```

### 📌 Notas
* No traduce áreas ya procesadas
* Optimizado para imágenes largas
* Funciona completamente offline
* Pensado para flujo real de scanlation


