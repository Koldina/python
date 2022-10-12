# Связующее звено
#import ex046_lec 
import ex046_lec_mnoz as ex046_lec
import ex046_lec_view



def button_click():# Опишим метод кнопки
    value_a = ex046_lec_view.get_value()
    value_b = ex046_lec_view.get_value()
    ex046_lec.init(value_a, value_b)
    #result = ex046_lec.sum()
    result = ex046_lec.mnoz()
    ex046_lec_view.view_data(result)