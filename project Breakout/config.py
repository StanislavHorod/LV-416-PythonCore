import colors
import random

screen_width = 800
screen_height = 600
choiser = random.uniform(1,4)
background_image = random.choice(['images/background1.jpg', 'images/background2.jpg','images/background3.jpg','images/background4.jpg'])


frame_rate = 90

row_count = int(random.uniform(5,12))
brick_width = 60
brick_height = 20
brick_color = colors.RED1
offset_y = brick_height + 10

ball_speed = 3
ball_radius = 8
ball_color = colors.GREEN1

platform_width = 60
platform_height = 15
platform_color = colors.ORANGE2
platform_speed = random.uniform(6, 12)

status_offset_y = 5

text_color =  colors.YELLOW1
initial_lives = 3
lives_right_offset = 85
lives_offset = screen_width - lives_right_offset
score_offset = 5

font_name = 'Arial'
font_size = 20

effect_duration = 20

sounds_effects = dict(
    brick_hit='sound_effects/brick_hit.wav',
    effect_done='sound_effects/effect_done.wav',
    paddle_hit='sound_effects/paddle_hit.wav',
    level_complete='sound_effects/level_complete.wav',
)

message_duration = 2

button_text_color = colors.BLACK,
button_normal_back_color = colors.BROWN1
button_hover_back_color = colors.GREY2
button_pressed_back_color = colors.GREY3

menu_offset_x = 20
menu_offset_y = 300
menu_button_w = 80
menu_button_h = 50
