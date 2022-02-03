from datetime import datetime
import numpy as np

def load_portfolio_dynamic_report(file_name):
    str2date = lambda x: datetime.strptime(x, '%d.%m.%Y %H:%M:%S')
    dynasset2float = lambda x: float(x.replace('\xa0', ''))

    col_names = "PortfolioDynamicsChartPortfolio,PortfolioDynamicsChartPortfolio_X,PortfolioDynamicsChartPortfolio_Y,textBox4,textBox7,PortfolioDynamicsPortfolioHeader,PortfolioDynamicsPortfolioData,PortfolioDynamicsAssetsHeader,PortfolioDynamicsAssetsData"

    return np.genfromtxt(file_name, encoding='utf-8', skip_header=1, skip_footer=3, dtype=None,
                         delimiter=",", names=col_names, converters={1: str2date, 8: dynasset2float})

def load_money_move_report(file_name):
    str2date = lambda x: datetime.strptime(x, '%d.%m.%Y')
    dynasset2float = lambda x: float(x.replace('\xa0', ''))

    col_names = "textBox26,textBox52,textBox53,textBox54,textBox1,textBox2,textBox3,textBox8,textBox9,textBox4,textBox5,textBox6,textBox7,textBox10,textBox11,textBox12,textBox13,textBox14,textBox15,textBox16,textBox17,textBox18,textBox19,textBox20,textBox21,textBox22,textBox23,textBox24,textBox25,textBox27,textBox28"

    report = np.genfromtxt(file_name, encoding='utf-8', skip_header=1, skip_footer=3, dtype=None,
                         delimiter=",", names=col_names, converters={14: str2date, 26: dynasset2float})

    return report