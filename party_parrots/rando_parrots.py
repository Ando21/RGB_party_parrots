# Program to select random party parrot GIFs
# And display it on the RGB matrix

# Be sure to get your party parrots here:
# https://cultofthepartyparrot.com/

# More info and hardware setup here:
# https://github.com/hzeller/rpi-rgb-led-matrix
# httpshttps://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/driving-matrices

# Imports
import os
import time
import random

# Paths
party_parrots_path = '/home/pi/RGB_party_parrots/party_parrots'
path_to_display_utility = '/home/pi/rpi-rgb-led-matrix/utils/led-image-viewer'

# Functions

def random_parrot_display(path_to_parrots=party_parrots_path,
                          time_per_image='5',
                          matrix_rows='32',
                          matrix_columns='64',
                          brightness='75', # 0 to 100
                          led_gpio_mapping='adafruit-hat'):
    
    '''Function to get all parrot gifs in directory,
        randomly pick one, display it on your RGB matrix
        for your selected time, and cycle'''
    
    # Make a list of GIFs to choose from given the provided path
    parrots = [file for file in os.listdir(party_parrots_path)]
    print(parrots)
    random.shuffle(parrots)
    # Make string to pass with command
    parrots = ' '.join(parrots)

    # Make settings string
    rows = '--led-rows=' + matrix_rows
    cols = '--led-cols=' + matrix_columns
    brightness = '--led-brightness=' + brightness
    mapping = '--led-gpio-mapping=' + led_gpio_mapping
    settings = 'sudo ' + path_to_display_utility + ' ' + rows + ' ' + cols + ' ' + mapping + ' ' + brightness + ' -t' + time_per_image + ' -f -w10 ' 

    # Create the command to run
    cmd = settings + parrots
    print(cmd)
    # Run command
    os.system(cmd)



random_parrot_display(path_to_parrots=party_parrots_path,
                      time_per_image='5',
                          matrix_rows='32',
                          matrix_columns='64',
                          led_gpio_mapping='adafruit-hat')
    
    