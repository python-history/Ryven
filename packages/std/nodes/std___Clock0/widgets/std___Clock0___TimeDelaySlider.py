# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QSlider


class TimeDelaySlider_PortInstanceWidget(QSlider):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(TimeDelaySlider_PortInstanceWidget, self).__init__(Qt.Horizontal)

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''
            background: transparent;
        ''')
        self.setFixedWidth(70)
        self.setMinimum(0)
        self.setMaximum(100000)
        self.setSingleStep(1)
        self.valueChanged.connect(self.slider_val_changed)


    def slider_val_changed(self):
        self.parent_node_instance.update_timer_interval((self.value()/self.maximum()))

    def get_val(self):
        return (self.value()/self.maximum())

    def get_data(self):
        data = {'val': self.value()}
        return data

    def set_data(self, data):
        self.setValue(data['val'])

    def removing(self):
        pass
