import flet as ft
from exif import Image


def main(page: ft.Page):
    def get_exif(image_path: str):
        with open(image_path, 'rb') as image_file:
            exif_im = Image(image_file)
        return exif_im
    
    def build_watermark(exif_im: Image):
        if not exif_im.has_exif:
            return ""
        print(dir(exif_im))
        print(exif_im.list_all())

        return f"{exif_im.datetime}\nCamera: {exif_im.make} {exif_im.model}\n{exif_im.focal_length}mm f/{exif_im.f_number} {exif_im.exposure_time}s ISO{exif_im.photographic_sensitivity}\nLens:  {exif_im.lens_model}"

        # {exif_im.lens_make} {exif_im.shutter_speed_value} {exif_im.aperture_value} {exif_im.brightness_value}

        #return f'{exif_im.datetime}{exif_dict["Zeroth"]["DateTime"]}\nCamera: {exif_dict["Make"]} {exif_dict["Model"]}\nLens: {exif_dict["LensMake"]} {exif_dict["LensModel"]}\n{exif_dict["ShutterSpeedValue"], {exif_dict["ApertureValue"]}}'

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