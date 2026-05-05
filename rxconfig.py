import reflex as rx
import os

config = rx.Config(
    app_name="portafolio",
    # GitHub Pages sirve el sitio bajo "/<repo>/". En local puedes dejar el default.
    frontend_path=os.getenv("FRONTEND_PATH", "/mi-portfolio")
)

