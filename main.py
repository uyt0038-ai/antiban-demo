from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

Window.clearcolor = (0.06, 0.06, 0.12, 1)


class AntiBanApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.is_active = False
        self.step = 0
        self.steps = [
            ("Đang khởi động...", 20),
            ("Kiểm tra bộ nhớ...", 40),
            ("Bypass scan...", 60),
            ("Ẩn tiến trình...", 80),
            ("✅ Hoàn tất!", 100),
        ]

        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical", padding=dp(20), spacing=dp(15))

        layout.add_widget(MDLabel(
            text="🛡️ ANTI-BAN",
            halign="center",
            font_style="H3",
            theme_text_color="Custom",
            text_color=(0, 1, 0.5, 1),
            size_hint_y=None,
            height=dp(70),
        ))

        card = MDCard(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(150),
            md_bg_color=(0.12, 0.12, 0.18, 1),
            radius=[dp(15)],
        )

        self.status_label = MDLabel(
            text="Chưa kích hoạt",
            theme_text_color="Custom",
            text_color=(0.8, 0.8, 0.8, 1),
            size_hint_y=None,
            height=dp(30),
        )
        self.progress = MDProgressBar(value=0, size_hint_y=None, height=dp(10))

        card.add_widget(self.status_label)
        card.add_widget(self.progress)
        layout.add_widget(card)

        self.toggle_btn = MDRaisedButton(
            text="BẬT BẢO VỆ",
            size_hint=(1, None),
            height=dp(60),
            md_bg_color=(0, 0.6, 0.4, 1),
        )
        self.toggle_btn.bind(on_release=self.toggle)
        layout.add_widget(self.toggle_btn)

        screen.add_widget(layout)
        return screen

    def toggle(self, *args):
        self.is_active = not self.is_active
        if self.is_active:
            self.toggle_btn.text = "TẮT BẢO VỆ"
            self.toggle_btn.md_bg_color = (1, 0.2, 0.3, 1)
            self.step = 0
            Clock.schedule_interval(self.update_progress, 0.9)
        else:
            self.toggle_btn.text = "BẬT BẢO VỆ"
            self.toggle_btn.md_bg_color = (0, 0.6, 0.4, 1)
            Clock.unschedule(self.update_progress)
            self.status_label.text = "Chưa kích hoạt"
            self.progress.value = 0

    def update_progress(self, dt):
        if self.step >= len(self.steps):
            Clock.unschedule(self.update_progress)
            return False
        msg, val = self.steps[self.step]
        self.status_label.text = msg
        self.progress.value = val
        self.step += 1


if __name__ == "__main__":
    AntiBanApp().run()
