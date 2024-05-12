from simulation import Simulation
import numpy as np
from pprint import pprint
import pandas as pd




def main():
    n_assets = 3
    n_trades = 1000
    sim = Simulation(n_assets, n_trades)
    trades,P = sim.simulate()

    base_sum = trades.groupby('base').sum()
    quote_sum = trades.groupby('quote').sum()
    E = (base_sum["baseQty"] - quote_sum["quoteQty"]).values

    x = np.linalg.solve(P,E)
    # pprint(x.round(2))
    resdf = pd.DataFrame({
        'exposure':E.round(2),
        'x':x.round(2),
    })
    pprint(resdf)
    print(pd.DataFrame(P.round(2)))
    print("Trade: Asset 0/{}")

    



if __name__ == '__main__':
    main()
