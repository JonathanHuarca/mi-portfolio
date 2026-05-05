# Portafolio - Jonathan Steve Huarca Alfaro

[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.5-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)
[![Vercel](https://img.shields.io/badge/Vercel-Deploy-black?style=for-the-badge&logo=vercel&logoColor=white&labelColor=101010)](https://vercel.com)

## 🌐 Portafolio web personal - Desarrollador Fullstack

Portafolio web minimalista y configurable, desarrollado con **Python** y **Reflex**, desplegado como sitio estático en **Vercel**.

### ✨ Características

- Avatar y datos principales
- Información de contacto y redes sociales
- Sección "Sobre mí"
- Tecnologías y herramientas
- Experiencia laboral detallada
- Proyectos destacados
- Formación académica
- Sección extra personalizable
- Tema oscuro configurable
- Diseño responsive

### 🛠️ Tecnologías utilizadas

| Backend | Frontend | Infraestructura |
|---------|----------|----------------|
| Python 3.10+ | Reflex 0.4.5 | Vercel (despliegue) |
| Reflex (framework web) | HTML/CSS/JS generado | Git (control de versiones) |

---

## 📦 Instalación local

### Requisitos previos

- Python 3.10 o superior
- Git

### Pasos

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/portafolio.git
cd portafolio

# Crear y activar entorno virtual
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux/Mac
# source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Inicializar y ejecutar
reflex init
reflex run
```

Abrir [http://localhost:3000](http://localhost:3000) en el navegador.

---

## ⚙️ Configuración

### 📝 Contenido

Editar el archivo `assets/data/data.json` con tu información personal:

```json
{
  "name": "Tu Nombre",
  "skill": "Tu especialidad",
  "about": "Descripción personal",
  "technologies": [...],
  "experience": [...],
  "projects": [...],
  "training": [...]
}
```

#### Iconos disponibles
- **Generales**: Identificadores de [Lucide Icons](https://lucide.dev/icons/)
- **Tecnologías**: Identificadores de [Devicon](https://devicon.dev/)

### 🎨 Tema visual

Para personalizar colores y apariencia:

1. Descomentar `rx.theme_panel()` en `portafolio/portafolio.py`
2. Ejecutar `reflex run`
3. Seleccionar configuración deseada en el panel
4. Pulsar "Copy Theme" y pegar en `rx.theme()`

---

## 🚀 Despliegue en Vercel

El proyecto incluye configuración lista para Vercel (`vercel.json` y `build.sh`).

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

O manualmente desde la CLI:

```bash
vercel --prod
```

---

## 📁 Estructura del proyecto

```
portafolio/
├── assets/              # Archivos estáticos
│   ├── data/
│   │   ├── data.json    # Datos del portafolio
│   │   └── cv.pdf       # Currículum vitae
│   ├── avatar.jpg       # Foto de perfil
│   ├── perfil-moventi.jpg
│   └── *.jpg            # Imágenes de proyectos
├── portafolio/          # Código fuente Python
│   ├── portafolio.py    # Punto de entrada
│   ├── data.py          # Carga de datos JSON
│   ├── views/           # Componentes de vista
│   ├── components/      # Componentes reutilizables
│   └── styles/          # Estilos y temas
├── rxconfig.py          # Configuración de Reflex
├── requirements.txt     # Dependencias
├── vercel.json          # Configuración de despliegue
└── build.sh             # Script de build
```

---

## 👤 Datos del portafolio

| Campo | Valor |
|-------|-------|
| **Nombre** | Jonathan Steve Huarca Alfaro |
| **Profesión** | Desarrollador Fullstack Mid-Senior |
| **Especialización** | Microservicios, Cloud Azure, Java/Spring Boot, .NET/C# |
| **Ubicación** | Lima, Perú |
| **Email** | jonathan.huarca@tecsup.edu.pe |
| **LinkedIn** | [linkedin.com/in/jonathanstevehuarca](https://linkedin.com/in/jonathanstevehuarca) |

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🙌 Agradecimientos

Proyecto basado en la plantilla original de [Brais Moure (mouredev)](https://github.com/mouredev/portafolio-template) - Portafolio "perfecto" para programadores.

---

<p align="center">Desarrollado con ❤️ por <a href="https://github.com/tuusuario">Jonathan Steve Huarca Alfaro</a></p>