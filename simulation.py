import numpy as np
import pandas as pd

from dataclasses import dataclass



@dataclass
class Simulation:
    """A class to simulate"""
    n_assets:int
    n_trades:int
    seed = 69

    
    def simulate(self):
        P = self.get_prices()

        base = np.random.choice(self.n_assets, self.n_trades)
        quote = np.random.choice(self.n_assets, self.n_trades)
        baseQty = np.random.randint(1, 100, self.n_trades)*0.1
        quoteQty = [baseQty[i]*P[base[i],quote[i]] for i in range(self.n_trades)]
        df = pd.DataFrame({'base':base, 'quote':quote, 'baseQty':baseQty, 'quoteQty':quoteQty})
        return df,P
        

    def get_prices(self):
        np.random.seed(self.seed)
        prices = np.abs(np.random.normal(1,0.5,(self.n_assets,self.n_assets)))
        np.fill_diagonal(prices,1.0)
        # make it symmetric reciprocal
        prices = (prices + prices.T)*0.5
        for i in range(self.n_assets):
            for j in range(self.n_assets):
                if i<j:
                    prices[j,i] = 1.0/prices[i,j]
        return prices
