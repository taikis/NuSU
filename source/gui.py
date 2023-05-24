import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)
import pathlib
import cut


def main(page: Page):
    # Selected files is now a list in the outer scope
    selected_files = []

    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files_text.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else None
        )
        # Clear and repopulate selected_files list
        selected_files.clear()
        selected_files.extend(e.files)
        selected_files_text.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files_text = Text()

    # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else None
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    def cut_and_save(_):
        for file in selected_files:
            cutter = cut.Cutter(file.path)
            cutter.save(pathlib.Path(directory_path.value))

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, get_directory_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files_text,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Open directory",
                    icon=icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                ),
                directory_path,
            ]
        ),
        Row(
            [
                ElevatedButton(
                    "Save file",
                    icon=icons.SAVE,
                    on_click=cut_and_save,
                    disabled=page.web,
                ),
            ]
        ),
    )


flet.app(target=main)
