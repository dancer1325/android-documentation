# Android Documentation Scraper

## ⚠️ IMPORTANTE: Consideraciones Legales y Éticas

**Este script es SOLO para uso educativo y personal.**

- La documentación de Android Developer está bajo **Creative Commons Attribution 2.5 License**
- Debes respetar los [Términos de Servicio de Google](https://policies.google.com/terms)
- NO uses esto para redistribuir la documentación sin la atribución apropiada
- El script incluye rate limiting para ser respetuoso con los servidores de Google

### Alternativas Recomendadas

1. **Repositorio oficial**: Google tiene documentación en GitHub que puedes clonar:
   - https://github.com/android/platform_docs

2. **Documentación offline oficial**: Puedes descargar la documentación a través de Android Studio SDK Manager

3. **Enlaces directos**: Para uso personal, considera simplemente enlazar a la documentación oficial

## Instalación

1. Instalar dependencias de Python:

```bash
pip install -r requirements.txt
```

O instalar directamente:

```bash
pip install requests beautifulsoup4 html2text lxml
```

## Uso

### Uso básico (límite de 100 páginas):

```bash
python scrape_android_docs.py
```

### Scrape de una sección específica:

```bash
# Solo la guía de arquitectura
python scrape_android_docs.py --url https://developer.android.com/guide/components --max-pages 50

# Solo Jetpack Compose
python scrape_android_docs.py --url https://developer.android.com/jetpack/compose --max-pages 30

# Solo Kotlin
python scrape_android_docs.py --url https://developer.android.com/kotlin --max-pages 40
```

### Opciones disponibles:

```bash
python scrape_android_docs.py --help
```

- `--url URL`: URL de inicio (por defecto: página principal de Android Developer)
- `--max-pages N`: Número máximo de páginas a descargar (por defecto: 100)
- `--delay SECONDS`: Segundos entre requests (por defecto: 2, mínimo recomendado: 1)
- `--output DIR`: Directorio de salida (por defecto: docsMirror)

### Ejemplos:

```bash
# Scraping rápido de una sección pequeña
python scrape_android_docs.py \
  --url https://developer.android.com/guide/components/activities \
  --max-pages 20 \
  --delay 1.5

# Scraping extenso con más paciencia
python scrape_android_docs.py \
  --max-pages 500 \
  --delay 3 \
  --output docsMirror
```

## Estructura de salida

El script crea archivos .md en `docsMirror/` que replican la estructura de URLs de developer.android.com:

```
docsMirror/
├── index.md
├── guide/
│   ├── components/
│   │   ├── activities.md
│   │   └── services.md
│   └── architecture/
│       └── viewmodel.md
└── jetpack/
    └── compose/
        └── tutorial.md
```

Cada archivo incluye:
- Título de la página
- Link a la fuente original
- Contenido convertido a Markdown

## Buenas prácticas

1. **Usa límites razonables**: No intentes descargar toda la documentación de una vez
2. **Respeta el rate limiting**: Mantén el delay en al menos 1-2 segundos
3. **Scraping selectivo**: Descarga solo las secciones que necesitas
4. **Atribución**: Si compartes o usas el contenido, mantén los links a la fuente original
5. **Actualización**: La documentación cambia; considera re-ejecutar periódicamente para secciones específicas

## Solución de problemas

### Error: "html2text not installed"
```bash
pip install html2text
```

### Error de conexión o timeout
- Aumenta el delay: `--delay 3`
- Verifica tu conexión a internet
- Algunos firewalls corporativos pueden bloquear el scraping

### Muchas páginas en blanco
- Algunas páginas requieren JavaScript para renderizar
- El contenido principal se extrae del HTML, si la página usa mucho JS dinámico puede fallar

## Licencia y atribución

El contenido descargado pertenece a Google y está bajo **Creative Commons Attribution 2.5 License**.

Cuando uses este contenido:
- Incluye atribución a Android Open Source Project
- Mantén los enlaces a la fuente original
- No redistribuyas sin la licencia apropiada

## Descargo de responsabilidad

Este script es una herramienta educativa. El usuario es responsable de:
- Cumplir con los términos de servicio de Google
- Usar el contenido de manera apropiada y legal
- Respetar las leyes de copyright aplicables

**Uso bajo tu propio riesgo.**
