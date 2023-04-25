import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.linear_model import LinearRegression



################# CAPM #################
# returns beta, alpha 
def capm(portfolio_returns, market_returns):
    x = market_returns.ravel().reshape(-1, 1)
    y = portfolio_returns.ravel().reshape(-1, 1)
    monthly_beta_regressor = LinearRegression()
    monthly_beta_regressor.fit(x, y)
    return monthly_beta_regressor.coef_.item(), monthly_beta_regressor.intercept_.item()

################# FF3 MODEL #################
# returns beta, alpha 
def ff3(portfolio_returns, ffm_data):
    x = (ffm_data[['Mkt-RF', 'HML', 'SMB']])/100
    #market_returns.ravel().reshape(-1, 1)
    y = portfolio_returns.ravel().reshape(-1, 1)
    monthly_beta_regressor = LinearRegression()
    monthly_beta_regressor.fit(x, y)
    
    # this value is the portfolio beta and alpha 
    return monthly_beta_regressor.coef_, monthly_beta_regressor.intercept_.item()