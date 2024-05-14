
Khánh Tôn Thất Phúc <khanh.ton2001@hcmut.edu.vn>
08:45 Th 5, 9 thg 5 (5 ngày trước)
đến Khanh

from yolobit import *

button_a.on_pressed = None

button_b.on_pressed = None

button_a.on_pressed_ab = button_b.on_pressed_ab = -1

from aiot_hcsr04 import HCSR04

from mqtt import *

from aiot_lcd1602 import LCD1602

import music

from homebit3_ir_receiver import *

from homebit3_rgbled import RGBLed

import time



aiot_lcd1602 = LCD1602()



homebit3_ir_rx = IR_RX(Pin(pin1.pin, Pin.IN)); homebit3_ir_rx.start();



tiny_rgb = RGBLed(pin14.pin, 4)



if True:

  aiot_ultrasonic = HCSR04(trigger_pin=pin10.pin, echo_pin=pin13.pin)

  m_E1_BA_ADt_kh_E1_BA_A9u_c_C3_A0i__C4_91_E1_BA_B7t = 'AABB'

  m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp = ''



while True:

  mqtt.connect_wifi('G', '22222222')

  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='dynabit', password='aio_pwOk91dqkDyvt8YV6zpwhC8LOOkn')

  mqtt.publish('topic', (temperature()))

  aiot_lcd1602.clear()

  aiot_lcd1602.move_to(0, 0)

  aiot_lcd1602.putstr('Temperature:')

  aiot_lcd1602.move_to(12, 0)

  aiot_lcd1602.putstr((temperature()))

  aiot_lcd1602.move_to(1, 1)

  aiot_lcd1602.putstr((aiot_ultrasonic.distance_cm()))

  if (aiot_ultrasonic.distance_cm()) < 3:

    display.show(Image.NO)

    aiot_lcd1602.move_to(9, 1)

    aiot_lcd1602.putstr('ALERT !!!')

    music.play(music.DADADADUM, wait=False)

  if (aiot_ultrasonic.distance_cm()) > 3:

    display.clear()

  if temperature() < 26:

    pin2.write_analog(round(translate(0, 0, 100, 0, 1023)))

  if homebit3_ir_rx.get_code() == IR_REMOTE_A:

    pin4.servo_write(270, max=270)

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_B:

    pin4.servo360_write(70)

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_C:

    pin4.servo_write(90)

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_F:

    pin2.write_analog(round(translate(70, 0, 100, 0, 1023)))

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_UP:

    pin2.write_analog(round(translate(100, 0, 100, 0, 1023)))

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_0:

    pin2.write_analog(round(translate(0, 0, 100, 0, 1023)))

    homebit3_ir_rx.clear_code()

  if homebit3_ir_rx.get_code() == IR_REMOTE_DOWN:

    pin2.write_analog(round(translate(30, 0, 100, 0, 1023)))

    homebit3_ir_rx.clear_code()

  if pin16.read_digital()==1:

    tiny_rgb.show(0, hex_to_rgb('#ff0000'))

  else:

    tiny_rgb.show(0, hex_to_rgb('#000000'))

  time.sleep_ms(1000)





aiot_lcd1602.backlight_on()



if temperature() >= 26:

  pin2.write_analog(round(translate(0, 0, 100, 0, 1023)))



if button_a.is_pressed():

  music.play(['G3:1'], wait=True)

  m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp = str(m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp) + 'A'

  aiot_lcd1602.clear()

  aiot_lcd1602.move_to(9, 1)

  aiot_lcd1602.putstr(m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp)

  time.sleep_ms(300)



if button_b.is_pressed():

  music.play(['G3:1'], wait=True)

  m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp = str(m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp) + 'B'

  aiot_lcd1602.clear()

  aiot_lcd1602.move_to(9, 1)

  aiot_lcd1602.putstr(m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp)

  time.sleep_ms(300)

if len(m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp) == 4:

  aiot_lcd1602.clear()

  if m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp == m_E1_BA_ADt_kh_E1_BA_A9u_c_C3_A0i__C4_91_E1_BA_B7t:

    aiot_lcd1602.move_to(9, 1)

    aiot_lcd1602.putstr('Xin moi vao')

    music.play(music.POWER_UP, wait=True)

    pin4.servo_write(90)

    time.sleep_ms(1000)

    pin4.servo_write(0)

    pin4.servo_release()

  else:

    aiot_lcd1602.move_to(9, 1)

    aiot_lcd1602.putstr('Sai mat khau')

    music.play(music.POWER_DOWN, wait=True)

  m_E1_BA_ADt_kh_E1_BA_A9u__C4_91_C3_A3_nh_E1_BA_ADp = ''

time.sleep_ms(300)