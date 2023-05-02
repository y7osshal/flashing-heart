basic.forever(function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playMelody("C D E F G A B C5 ", 128)
    music.playMelody("C5 A B G A F G E ", 120)
    basic.showIcon(IconNames.SmallSquare)
    radio.setGroup(1)
    led.plot(2, 3)
    music.setVolume(255)
})
