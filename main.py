import matplotlib.pyplot as plt

import loaders

portfolio_dynamic_report = loaders.load_portfolio_dynamic_report("PortfolioDynamicsReport.csv")

x = portfolio_dynamic_report["PortfolioDynamicsChartPortfolio_X"]
y = portfolio_dynamic_report["PortfolioDynamicsAssetsData"]

for date, value in zip(x, y):
    print(date, "\t", value)

plt.plot(x, y)
# plt.yticks(np.arange(min(y), max(y)+1, 100 * 1000))
plt.grid()
plt.show()
