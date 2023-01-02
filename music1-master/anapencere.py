import re

from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from api import getTrack
from functions.song_information import get_statics
import pyqtgraph as pg
import csv


class AnapencerePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.plot = pg.plot()
        self.anapencerecheck = Ui_MainWindow()
        self.anapencerecheck.setupUi(self)
        self.anapencerecheck.searchButton.clicked.connect(self.get_singer)
        self.anapencerecheck.songWidget.clicked.connect(self.get_detail)
        self.anapencerecheck.graphLayout.addWidget(self.plot)
        self.href = []
        self.bargraph = None
        self.header = ["title",'view', 'like', 'repost', 'comment']
    def get_singer(self):
        self.href = []
        self.anapencerecheck.songWidget.clear()
        singer = self.anapencerecheck.lineEdit.text()
        song = getTrack(singer)
        for i in song:
            self.anapencerecheck.songWidget.addItem(i["title"])
            self.href.append(i["link"])

    def get_detail(self):

        if (self.bargraph):
            self.plot.removeItem(self.bargraph)
        try:
            row = self.anapencerecheck.songWidget.currentRow()
            data = get_statics(self.href[row])
            likes_number = int("".join(re.findall(r"\d+", data[0]["likes"])))
            view_number = int("".join(re.findall(r"\d+", data[0]["view"])))
            comment_number = int("".join(re.findall(r"\d+", data[0]["comment"])))
            repost_number = int("".join(re.findall(r"\d+", data[0]["repost"])))
            y1 = [view_number, likes_number, comment_number, repost_number]
            xlab = ["view", "likes", "comment", "repost"]
            xval = list(range(1, len(xlab) + 1))
            ticks = []
            for i, item in enumerate(xlab):
                ticks.append((xval[i], item))
            ticks = [ticks]
            self.bargraph = pg.BarGraphItem(x=xval, height=y1, width=0.6, brush='b')
            self.plot.addItem(self.bargraph)
            ax = self.plot.getAxis('bottom')
            ax.setTicks(ticks)
            likes = ".".join(re.findall(r"\d+", data[0]["likes"]))
            view = ".".join(re.findall(r"\d+", data[0]["view"]))
            comment = ".".join(re.findall(r"\d+", data[0]["comment"]))
            repost = ".".join(re.findall(r"\d+", data[0]["repost"]))
            self.anapencerecheck.like_area.setText(likes)
            self.anapencerecheck.view_area.setText(view)
            self.anapencerecheck.comment_area.setText(comment)
            self.anapencerecheck.respost_area.setText(repost)
            print(data)
            with open('songs.csv', 'a',newline="\n" ,encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow([data[0]["url"], view_number, likes_number, repost_number, comment_number])
        except:
            self.anapencerecheck.like_area.setText("No information")
            self.anapencerecheck.view_area.setText("No information")
            self.anapencerecheck.comment_area.setText("No information")
            self.anapencerecheck.respost_area.setText("No information")
