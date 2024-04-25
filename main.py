import flet as ft
import requests


def main(page: ft.Page):
    page.tittle = "Погода"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    weather_data = ft.Text('')
    weather_data2 = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 2:




            return

        API = 'ae2ab37925b0a79610e8146830fa8b07'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        feelTemp = res['main']['feels_like']
        weather_data.value = 'Температура ' + str(temp)
        weather_data2.value = 'Ощущается как ' + str(feelTemp)
        page.update()

    def change_them(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_them),
                ft.Text('Погода')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='получить', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data2], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
