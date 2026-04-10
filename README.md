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

- 📂 Soporte para imágenes largas (manhwa/webtoon)
- ✂️ Selección manual de múltiples áreas
- 🤖 OCR + traducción automática con IA local
- 📝 Edición manual del texto traducido
- 🎯 Texto reposicionado automáticamente en su lugar original
- 🧠 Evita retraducir áreas ya procesadas
- 📤 Exportación final como imagen
- 🧩 Código modular (fácil de extender)

---

## ⚙️ Cómo funciona

1. Cargar imagen  
2. Seleccionar áreas de texto  
3. Presionar **Traducir**  
4. Editar texto si es necesario  
5. Exportar imagen final  

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
* Asegúrate de tener LM Studio corriendo en:
```bash
verifica http://localhost:1234
```
* inicia el sv manualmente en cmd con:
```bash
lms server start
```
* Modelo Probado:
```bash
gemma-3-4b
```
⚠️ Debe ser una versión compatible con imágenes

### 🎨 Personalización
* Para cambiar la fuente ve a "text_render.py" cambia "comic.ttf" por tu fuente.
```bash
  font = ImageFont.truetype("comic.ttf", font_size)
```

### 🧠 Flujo de trabajo
* Cargar imagen
* Seleccionar áreas de texto
* Presionar "Traducir"
* Editar texto si es necesario
* Exportar imagen final

### 📌 Notas
* No traduce áreas ya procesadas
* Optimizado para imágenes largas
* Funciona completamente offline
* Pensado para flujo real de scanlation


