from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
import requests
import yt_dlp

# Set Window Size for Development
Window.size = (350, 600)

# Kivy KV Design
KV = """
ScreenManager:
    MainScreen:
    DownloadScreen:

<MainScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "StreamSaver"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0.5, 0.8, 1
            font_style: "H4"

        MDLabel:
            text: "Download Videos, Songs, MP3 & MP4 with Ease"
            halign: "center"
            theme_text_color: "Secondary"

        MDTextField:
            id: url_input
            hint_text: "Enter URL here"
            icon_right: "link"
            mode: "rectangle"

        MDRaisedButton:
            text: "Download"
            pos_hint: {"center_x": 0.5}
            on_release: 
                app.start_download(url_input.text)

<DownloadScreen>:
    name: "download"

    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "Download in Progress..."
            halign: "center"
            theme_text_color: "Secondary"

        MDProgressBar:
            id: progress_bar
            value: 0
            max: 100

        MDRaisedButton:
            text: "Back to Home"
            pos_hint: {"center_x": 0.5}
            on_release: app.return_to_home()
"""

# Define Screens
class MainScreen(Screen):
    pass

class DownloadScreen(Screen):
    pass

# StreamSaver App
class StreamSaverApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def start_download(self, url):
        if not url:
            self.show_dialog("Error", "Please enter a valid URL.")
            return

        self.root.current = "download"

        def download_media():
            try:
                ydl_opts = {
                    'progress_hooks': [self.update_progress],
                    'outtmpl': '%(title)s.%(ext)s',
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except Exception as e:
                self.show_dialog("Download Failed", str(e))
                self.root.current = "main"

        from threading import Thread
        Thread(target=download_media).start()

    def update_progress(self, d):
        if d['status'] == 'downloading':
            progress = d['_percent_str'].strip('%')
            self.root.get_screen('download').ids.progress_bar.value = float(progress)
        elif d['status'] == 'finished':
            self.show_dialog("Success", "Download Complete!")
            self.root.current = "main"

    def return_to_home(self):
        self.root.current = "main"

    def show_dialog(self, title, text):
        if not hasattr(self, 'dialog') or not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: self.dialog.dismiss())],
            )
        else:
            self.dialog.title = title
            self.dialog.text = text
        self.dialog.open()

# Run the App
if __name__ == "__main__":
    StreamSaverApp().run()
