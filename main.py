from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.core.audio import SoundLoader
from kivy.core.window import Window


from random import random

Window.clearcolor = 1, 1, 1, 1
Window.icon = 'media/numbers/toys-icon.png'

class NumerosWindow(Screen):
    def contar(self):
        clicks = int(self.ids['contar_btn'].text)
        if clicks == 10:
            clicks = 0
        self.ids['contar_btn'].text = str(clicks + 1)
        return self.ids['contar_btn']

    def num_btn_txt(self):
        num_btn = self.ids['contar_btn']
        number = 1
        num_btn.text = str(number)
        return num_btn.text

    def set_numeros_image(self):
        clicks = int(self.ids['contar_btn'].text)-1

        images = ['media/numbers/01.jpg',
                  'media/numbers/02.jpg',
                  'media/numbers/03.jpg',
                  'media/numbers/04.jpg',
                  'media/numbers/05.jpg',
                  'media/numbers/06.jpg',
                  'media/numbers/07.jpg',
                  'media/numbers/08.jpg',
                  'media/numbers/09.jpg',
                  'media/numbers/10.jpg']

        display_image = self.ids.num_image

        for image in images:
            image = images[clicks]
        display_image.source = image

        return image


class ImageButton(ButtonBehavior, Image):
    pass

class ColoresWindow(Screen):
    def audio_violeta(self):
        sound = SoundLoader.load('media/audio/colores_violeta.wav')
        sound.play()

    def audio_amarillo(self):
        sound = SoundLoader.load('media/audio/colores_amarillo.wav')
        sound.play()

    def audio_verde(self):
        sound = SoundLoader.load('media/audio/colores_verde.wav')
        sound.play()

    def audio_azul(self):
        sound = SoundLoader.load('media/audio/colores_azul.wav')
        sound.play()

    def audio_marron(self):
        sound = SoundLoader.load('media/audio/colores_marron.wav')
        sound.play()

    def audio_naranja(self):
        sound = SoundLoader.load('media/audio/colores_naranja.wav')
        sound.play()

    def audio_rosa(self):
        sound = SoundLoader.load('media/audio/colores_rosa.wav')
        sound.play()

    def audio_rojo(self):
        sound = SoundLoader.load('media/audio/colores_rojo.wav')
        sound.play()

class AnimalesWindow(Screen):
    def audio_oso(self):
        sound = SoundLoader.load('media/audio/bear.wav')
        sound.play()

    def audio_cerdo(self):
        sound = SoundLoader.load('media/audio/pig_oink.wav')
        sound.play()

    def audio_pato(self):
        sound = SoundLoader.load('media/audio/duck.wav')
        sound.play()

    def audio_lobo(self):
        sound = SoundLoader.load('media/audio/wolf_howl.wav')
        sound.play()

    def audio_elefante(self, *args):
        sound = SoundLoader.load('media/audio/elephant.wav')
        sound.play()

    def audio_gato(self):
        sound = SoundLoader.load('media/audio/cat_meow.wav')
        sound.play()

    def audio_leon(self):
        sound = SoundLoader.load('media/audio/lion_roar.wav')
        sound.play()

    def audio_mono(self):
        sound = SoundLoader.load('media/audio/monkey_excited.wav')
        sound.play()

    def audio_gallo(self):
        sound = SoundLoader.load('media/audio/rooster.wav')
        sound.play()

    def audio_vaca(self):
        sound = SoundLoader.load('media/audio/cow_moo.wav')
        sound.play()

    def audio_rana(self):
        sound = SoundLoader.load('media/audio/frog.wav')
        sound.play()

    def audio_perro(self):
        sound = SoundLoader.load('media/audio/dog_bark.wav')
        sound.play()


class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class PaintWindow(Screen):
    pass


class PaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y), width=1.5)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def clear_canvas(self):
        self.canvas.clear()


kv = Builder.load_file("Babies.kv")

class BabiesApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    BabiesApp().run()