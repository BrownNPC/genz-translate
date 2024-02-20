from translator import translate
import flet as ft



class ZoomerTranslate(ft.UserControl):


    def build(self):

        async def on_change_zoomer(e):
            english_textfield.value = translate(e.control.value)
            await self.update_async()
        async def on_change_english(e):
            zoomer_textfield.value = translate(e.control.value, to_genz=True)
            await self.update_async()

        if self.page.window_width:
            page_width = self.page.window_width
        else:
            page_width=self.page.width
        zoomer_textfield = ft.TextField(width=page_width/2-20,min_lines=10, max_lines=10, multiline=True, on_change=on_change_zoomer)
        english_textfield = ft.TextField(width=page_width/2-20,min_lines=10, max_lines=10, multiline=True, on_change=on_change_english)


        return ft.Row(
            spacing=10,
            controls=[
            ft.Column([
            ft.Container(
                ft.Text('English', size=20)),
            ft.Container(english_textfield),]),
            ft.Column([
            ft.Container(
                ft.Text('Zoomer (Simplified)', size=20)),
            ft.Container(zoomer_textfield),
            ]),
        ]
        )


async def main(page: ft.Page):

    page.theme_mode=ft.ThemeMode.LIGHT
    await page.add_async(
        ft.Row([
            ft.Container(width=240,height=100, content=ft.Image('icon.png')),
            ft.Text('Translate', size=60)
        ])
    )

    await page.add_async(ZoomerTranslate())
    

    await page.update_async()

ft.app(main, port=8080)