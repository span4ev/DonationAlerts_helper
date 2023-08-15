from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QVBoxLayout, QLabel, QSpinBox, QSlider, QLineEdit
from PyQt5.QtGui import QIntValidator
from PyQt5 import uic
from da import DA
import os

class App(QDialog):
    def __init__(self):
        super().__init__()

        uic.loadUi('class.ui', self)

        self.config_file = 'config.txt'
        self.config = self.get_config()

        self.default_settings = {
            'script_option': [1, (1, 2)], 
            'sorting': [3, (1, 5)], 
            'min_donation_sum': [0, (0, 10000)],
            'donations_lines_amount': [0, (0, 10000)], 
            'total_sum': [1, (0, 1)], 
            'line_ending': '', 
            'show_donation_date' : [0, (0, 1)]
        }
        self.script_option          = self.default_settings['script_option'][0]
        self.sorting                = self.default_settings['sorting'][0]
        self.min_donation_sum       = self.default_settings['min_donation_sum'][0]
        self.donations_lines_amount = self.default_settings['donations_lines_amount'][0]
        self.total_sum              = self.default_settings['total_sum'][0]
        self.line_ending            = self.default_settings['line_ending']
        self.show_donation_date     = self.default_settings['show_donation_date'][0]

        self.btn_script_options = [self.findChild(QRadioButton, f'btn_script_options_{i}') for i in range(1, 3)]
        self.btn_sorting = [self.findChild(QRadioButton, f'btn_sorting_{i}') for i in range(1, 6)]
        self.btn_total_sum = [self.findChild(QRadioButton, f'btn_total_sum_{i}') for i in range(0, 2)]
        self.btn_show_donation_date = [self.findChild(QRadioButton, f'btn_show_donation_date_{i}') for i in range(0, 2)]
        for btn in self.btn_sorting + self.btn_script_options + self.btn_total_sum + self.btn_show_donation_date:
            btn.toggled.connect(self.btn_toggled)

        self.var_to_widget_mapping = {
            'script_option': self.btn_script_options,
            'sorting': self.btn_sorting,
            'min_donation_sum': self.spinBox_min_donation_sum,
            'donations_lines_amount': self.spinBox_donations_lines_amount,
            'total_sum': self.btn_total_sum,
            'line_ending': self.lineEdit_line_ending,
            'show_donation_date': self.btn_show_donation_date,
        }



        self.read_config()
        self.update_widget_values()


        self.spinBox_min_donation_sum.setRange(0, 9999)
        self.slider_min_donation_sum.setRange(0, 9999)
        self.spinBox_donations_lines_amount.setRange(0, 9999)
        self.slider_donations_lines_amount.setRange(0, 9999)
        self.slider_min_donation_sum.valueChanged.connect(self.spinBox_min_donation_sum.setValue)
        self.spinBox_min_donation_sum.valueChanged.connect(lambda value: setattr(self, 'min_donation_sum', value))
        self.slider_donations_lines_amount.valueChanged.connect(self.spinBox_donations_lines_amount.setValue)
        self.spinBox_donations_lines_amount.valueChanged.connect(lambda value: setattr(self, 'donations_lines_amount', value))

        self.btn_reset.clicked.connect(self.reset_values)
        self.btn_ok.clicked.connect(self.btn_ok_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)



    def get_config(self):

        if os.path.exists(self.config_file):
            with open (self.config_file, 'r', encoding='utf-8') as f:
                return f.readlines()
        else:
            return []

    def read_config(self):

        self.config = [i.strip() for i in self.config]

        for i in self.config:
            i = i.split('=')
            var = i[0].strip()
            val = i[1].strip()

            if val.isdigit():
                val         = int(val)
                default_val = self.default_settings[var][0]
                min_val     = self.default_settings[var][1][0]
                max_val     = self.default_settings[var][1][1]

                if var == 'script_option': 
                    if min_val <= val <= max_val:
                        self.script_option = val
                    else:
                        self.script_option = default_val

                if var == 'sorting':
                    if min_val <= val <= max_val:
                        self.sorting = val
                    else:
                        self.sorting = default_val

                if var == 'min_donation_sum':
                    if min_val <= val <= max_val:
                        self.min_donation_sum = val
                    else:
                        self.min_donation_sum = default_val

                if var == 'donations_lines_amount':
                    if min_val <= val <= max_val:
                        self.donations_lines_amount = val
                    else:
                        self.donations_lines_amount = default_val
                
                if var == 'total_sum':
                    if min_val <= val <= max_val:
                        self.total_sum = val
                    else:
                        self.total_sum = default_val

                if var == 'show_donation_date':
                    if min_val <= val <= max_val:
                        self.show_donation_date = val
                    else:
                        self.show_donation_date = default_val            

            else:
                if var == 'line_ending':
                    self.line_ending = val

        self.update_widget_values()


    def update_widget_values(self):
        for var, widget in self.var_to_widget_mapping.items():
            if isinstance(widget, list):
                self.set_selected_radio_button(widget, getattr(self, var))
            elif isinstance(widget, QSpinBox) or isinstance(widget, QSlider):
                widget.setValue(getattr(self, var))
            elif isinstance(widget, QLineEdit):
                widget.setText(getattr(self, var))


    def set_selected_radio_button(self, radio_button_list, value):
        for btn in radio_button_list:
            if btn.objectName().endswith(str(value)):
                btn.setChecked(True)
                break


    def btn_ok_clicked(self):

        self.script_option = self.get_selected_radio_button_value(self.btn_script_options)
        self.sorting = self.get_selected_radio_button_value(self.btn_sorting)
        self.total_sum = self.get_selected_radio_button_value(self.btn_total_sum)
        self.show_donation_date = self.get_selected_radio_button_value(self.btn_show_donation_date)
        self.line_ending = self.lineEdit_line_ending.text() # текст из QLineEdit

        self.create_config_file()
        self.accept()


        da = DA(self.script_option, 
                self.sorting, 
                self.min_donation_sum, 
                self.donations_lines_amount, 
                self.total_sum, 
                self.line_ending, 
                self.show_donation_date)
        da.start()


    def btn_cancel_clicked(self):

        self.accept()


    def reset_values(self):
        self.script_option = self.default_settings['script_option'][0]
        self.sorting = self.default_settings['sorting'][0]
        self.min_donation_sum = self.default_settings['min_donation_sum'][0]
        self.donations_lines_amount = self.default_settings['donations_lines_amount'][0]
        self.total_sum = self.default_settings['total_sum'][0]
        self.line_ending = self.default_settings['line_ending']
        self.show_donation_date = self.default_settings['show_donation_date'][0]

        self.update_widget_values()

    def get_selected_radio_button_value(self, radio_button_list):
        for btn in radio_button_list:
            if btn.isChecked():
                return btn.objectName().split('_')[-1]
        return None
    

    def btn_toggled(self):

        selected_btn = self.sender()
        if selected_btn.isChecked():
            btn_name = selected_btn.objectName()
            parts = btn_name.rsplit('_', 1)
            if len(parts) == 2:
                btn_type, btn_value = parts
                if btn_type == 'btn_script_options':
                    self.script_option =  btn_value
                if btn_type == 'btn_sorting':
                    self.sorting = btn_value
                if btn_type == 'btn_total_sum':
                    self.total_sum = btn_value
                if btn_type == 'btn_show_donation_date':
                    self.show_donation_date = btn_value
            else:
                print(f'Хуйня какая-то...: {btn_name}')



    def create_config_file(self):

        with open (self.config_file, 'w', encoding='utf-8') as f:
            f.write(f'script_option = {self.script_option}\n')
            f.write(f'sorting = {self.sorting}\n')
            f.write(f'min_donation_sum = {self.min_donation_sum}\n')
            f.write(f'donations_lines_amount = {self.donations_lines_amount}\n')
            f.write(f'line_ending = {self.line_ending}\n')
            f.write(f'total_sum = {self.total_sum}\n')
            f.write(f'show_donation_date = {self.show_donation_date}')

