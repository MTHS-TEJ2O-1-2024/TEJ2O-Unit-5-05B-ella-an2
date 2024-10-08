/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Ella
 * Created on: Oct 2024
 * This program is a traffic light
*/

let neopixelLight: neopixel.Strip = null

basic.clearScreen()
neopixelLight = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
neopixelLight.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
neopixelLight.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
neopixelLight.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
neopixelLight.show()
basic.showIcon(IconNames.Happy)

