import flet as ft


def main(page: ft.Page):


    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
        filepaths = [f.path for f in e.files] if e.files else []

        for file in filepaths:
            img = ft.Image(
                src=file,
                width=300,
                height=300,
                #fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
            images.controls.append(img)
            exif = get_exif(file)
            watermark = build_watermark(exif)
            images.controls.append(ft.Text(watermark))

        page.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True,
                        file_type=ft.FilePickerFileType.IMAGE
                    ),
                ),
                selected_files,
            ]
        )
    )
    page.add(images)


ft.app(target=main)