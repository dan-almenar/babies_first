# babies_first
A small app I made for my 2yo baby daughter (python + kivy). This is actually my first full project since I decided to dive into programming on late february.

Being my very first app I am aware the coding may have a lot of room for improvement. The very first disclaimer I have to make in this regard is the the code
is written in a mix of English and Spanish, a terrible idea that I hope I get fixed on subsequent commits.

However, it does the job I had in mind which was creating a Python + Kivy app
that I could later on pack into an Android APK.

The app has 4 very simple modules (screens):
1. Numbers: A screen with an image displaying a number from 1 to 10 aside a button with said number as a label. Whenever the button is released its label and the
image change accordingly.
2. Colors: A display of 8 buttons, each with a different color. the on_release method of wich triggers an audio file that says the color's name.
3. Animals: Same logic behind the colors module, with the difference that each button has an image and the audio file triggered is not the animal's name but it's
natural sound.
4. Painting: Almost an exact copy of the Kivy's A Simple Paint App tutorial (https://kivy.org/doc/stable/tutorials/firstwidget.html) with very small differences.

I commited just the .py and .kv file I do not own the rights for any of the images or the audio files I used.

I'm sure the colors and animals modules may be redone using the kivy's recycleview feature, yet I'm still trying to understand it. If I get it done, I'll commit the changes.

Again, this is my first project, though this is my first github commit. If this README.md file doesn't comply to what's expected, please let me know.
