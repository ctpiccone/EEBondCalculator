# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import pandas as pd


class Bond:
    def __init__(self, price, month, year):
        self.issue = datetime.datetime(year, month, 1)
        self.price = price

    def calculate(self, end_date):
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        date = self.issue
        # calculate first non-six month period
        # get next recalc-period
        time_delta = min([abs(date - d) for d in list(get_rates().index) if d > date])
        next_date = [d for d in list(get_rates().index) if abs(date - d) == time_delta][0]
        value = self.price*(1+get_rate(date)*(next_date.month-date.month)/12)
        time_delta = min([abs(date - d) for d in list(get_rates().index) if d > next_date])
        date = [d for d in list(get_rates().index) if abs(date - d) == time_delta][0]
        while True:
            time_delta = min([abs(date - d) for d in list(get_rates().index) if d > date])
            date = [d for d in list(get_rates().index) if abs(date - d) == time_delta][0]
            if date > end_date:
                break
            value = value * (1 + get_rate(date) / 2)


def get_rates():
    return pd.read_csv("rates.csv", parse_dates=["Date"], index_col="Date")


def get_rate(date_target):
    if not type(date_target) == datetime.datetime and not type(date_target) == pd._libs.tslibs.timestamps.Timestamp:
        date_target = datetime.datetime.strptime(date_target, "%Y-%m-%d")
    rates = pd.read_csv("rates.csv", parse_dates=["Date"], index_col="Date")
    # get closest date
    time_delta = min([abs(date_target - date) for date in list(rates.index) if
                      date < date_target])
    return float(
        rates.loc[[date for date in list(rates.index) if abs(date_target - date) == time_delta][0]].iloc[0][:-1]) / 100


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = Bond(25, 3, 2003)
    b.calculate("2022-08-01")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
