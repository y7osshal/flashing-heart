def on_forever():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    music.play_melody("C D E F G A B C5 ", 128)
    music.play_melody("C5 A B G A F G E ", 120)
    basic.show_icon(IconNames.SMALL_SQUARE)
    radio.set_group(1)
    led.plot(2, 3)
    music.set_volume(255)
basic.forever(on_forever)
