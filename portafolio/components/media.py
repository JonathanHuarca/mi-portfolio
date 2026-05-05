import reflex as rx
from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True
        ),
        rx.hstack(
            icon_button(
                "file-text",
                rx.asset(data.cv.lstrip("/")),
                download_filename="Jonathan_Huarca_CV.pdf",
            ),
            icon_button(
                "folder_git_2",
                data.github
            ),
            icon_button(
                "external_link",
                data.likedin
            ),
            spacing=Size.SMALL.value
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"]
    )
