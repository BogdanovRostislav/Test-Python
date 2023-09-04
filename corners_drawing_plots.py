import pandas as pd
import matplotlib.pyplot as plt
import os

class drawing_plots:
    def __init__(self) -> None:
        self.deviation_json = pd.DataFrame()
        self.path = []
        pass
    def draw_plots(self):
        self.deviation_json = pd.read_json('deviation.json')
        for i in self.deviation_json.columns[1:]:
            plt.plot(self.deviation_json[i])
            plt.xlabel(i)
            plt.savefig('plots/' + i)
            plt.show()
            self.path.append(os.path.realpath('plots/' + i))
        return self.path
    def describe(self):
        return self.deviation_json.describe()