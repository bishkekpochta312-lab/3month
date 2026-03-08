import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    greeting_history = []
    history_text = ft.Text("greet history")

    def on_click_func(_):
        print(name_input.value)
        name = name_input.value
        if name:
            text_hello.value = f'Hello {name}'
            text_hello.color = None
            greeting_history.append(name)
            history_text.value = "greet_history:\n" + "\n".join(greeting_history)
            # print(greeting_history)
        else:
            text_hello.value = "Write correct name"
            text_hello.color = ft.Colors.RED
        name_input.value = None
        page.update()

        name_input.label = "Success"

    page.title = "My first app"
    text_hello = ft.Text(value = "Hello")
    text_hello.value = "Privet Mir"
    name_input = ft.TextField(label="write name", expand = True,on_submit=on_click_func)

    elevated_button = ft.ElevatedButton("send",icon=ft.Icons.SEND,color=ft.Colors.GREEN, on_click=on_click_func)
    def edit_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def delete_all(_):
        greeting_history.clear()
        history_text.value = "greet history"
        page.update()
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE,on_click = delete_all)

    main_objects = ft.Row([name_input,elevated_button,theme_button,delete_button],alignment = ft.MainAxisAlignment.CENTER)

    page.add(text_hello,main_objects,history_text)



ft.app(main)

# ft.app(main,view = ft.AppView.WEB_BROWSER)
