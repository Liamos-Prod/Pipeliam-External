from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsOpacityEffect
from PySide6.QtCore import QPropertyAnimation, QEasingCurve

from functions.ui_functions import show_message_status_bar

#SPLASHSCREEN
def fade_widget(widget, duration=500, fade_in=True):
    effect = QGraphicsOpacityEffect()
    widget.setGraphicsEffect(effect)
    anim = QPropertyAnimation(effect, b"opacity")
    anim.setDuration(duration)
    anim.setStartValue(0.0 if fade_in else 1.0)
    anim.setEndValue(1.0 if fade_in else 0.0)
    anim.setEasingCurve(QEasingCurve.InOutQuad)
    anim.start()
    return anim  # Garde-le vivant si nécessaire


frame_states = {}
frame_animations = {}

def toggle_frame_visibility(frame, minWidth, maxWidth,statusbar=None):
    if frame not in frame_states:
        frame_states[frame] = False
    def toggle():
        if frame_states[frame]:
            collapse_frame(frame, minWidth, maxWidth)
            show_message_status_bar(statusbar,"Collapsed Frame")
        else:
            expand_frame(frame, minWidth, maxWidth)
            show_message_status_bar(statusbar,"Expanded Frame")
    return toggle

def expand_frame(frame, minWidth, maxWidth):
    if frame not in frame_animations:
        animation = QPropertyAnimation(frame, b'maximumWidth')
        animation.setDuration(250)
        animation.setStartValue(minWidth)
        animation.setEndValue(maxWidth)
        animation.setEasingCurve(QEasingCurve.OutBack)
        frame_animations[frame] = animation

    frame_animations[frame].setDirection(QPropertyAnimation.Forward)
    frame_animations[frame].start()

    frame_states[frame] = True

def collapse_frame(frame, minWidth, maxWidth):
    if frame not in frame_animations:
        animation = QPropertyAnimation(frame, b'maximumWidth')
        animation.setDuration(250)
        animation.setStartValue(maxWidth)
        animation.setEndValue(minWidth)
        animation.setEasingCurve(QEasingCurve.InBack)
        frame_animations[frame] = animation

    frame_animations[frame].setDirection(QPropertyAnimation.Backward)
    frame_animations[frame].start()

    frame_states[frame] = False