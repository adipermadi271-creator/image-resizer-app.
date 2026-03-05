from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from PIL import Image

class ResizerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        layout.add_widget(MDLabel(text="Ubah Resolusi Gambar", halign="center", font_style="H5"))
        
        self.path = MDTextField(hint_text="Nama file (contoh: foto.jpg)")
        layout.add_widget(self.path)
        
        self.width_in = MDTextField(hint_text="Lebar Baru (px)", input_filter="int")
        layout.add_widget(self.width_in)
        
        self.height_in = MDTextField(hint_text="Tinggi Baru (px)", input_filter="int")
        layout.add_widget(self.height_in)
        
        btn = MDRaisedButton(text="PROSES & SIMPAN", pos_hint={"center_x": .5}, on_release=self.ubah_foto)
        layout.add_widget(btn)
        
        screen.add_widget(layout)
        return screen

    def ubah_foto(self, *args):
        try:
            img = Image.open(self.path.text)
            new_size = (int(self.width_in.text), int(self.height_in.text))
            resized = img.resize(new_size, Image.Resampling.LANCZOS)
            resized.save("HASIL_RESIZE.jpg")
            self.path.text = "Berhasil! Tersimpan: HASIL_RESIZE.jpg"
        except Exception as e:
            self.path.text = f"Gagal: {str(e)}"

if __name__ == "__main__":
    ResizerApp().run()
