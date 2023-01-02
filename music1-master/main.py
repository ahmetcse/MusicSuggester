from PyQt5.QtWidgets import QApplication
from anapencere import AnapencerePage


app=QApplication([])
pencere=AnapencerePage()
pencere.show()
app.exec_()