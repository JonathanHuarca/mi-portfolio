import reflex as rx


def icon_button(
    icon: str,
    url: str,
    text: str = "",
    solid: bool = False,
    download_filename: str = "",
) -> rx.Component:
    """Button that navigates to a URL or triggers a download for internal assets."""
    # Normalize internal hrefs so they don't become relative (e.g. /mi-portfolio/mi-portfolio/...).
    is_external = url.startswith(("http://", "https://", "mailto:"))
    href = url if is_external or url.startswith("/") else f"/{url}"

    button = rx.button(
        rx.icon(icon),
        text,
        variant="solid" if solid else "surface",
    )

    if download_filename:
        return rx.button(
            rx.icon(icon),
            text,
            variant="solid" if solid else "surface",
            on_click=rx.download(url=href, filename=download_filename),
        )

    return rx.link(
        button,
        href=href,
        is_external=is_external,
    )
