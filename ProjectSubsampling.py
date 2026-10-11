#using subsampling with random groups

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
#loading the data
df = pd.read_csv('india_data.csv')       
x = df['year'].values                    
y = df['fertility_rate_hist'].values     

#putting the line of best fit (for comparison later)

slope_all, intercept_all = np.polyfit(x, y, 1)      # fit y = slope * year + intercept
pred_all = slope_all * 2050 + intercept_all         # extend the line to 2050
print(f"Fit on all data: prediction for 2050 = {pred_all:.3f}")


#subsampling
#using random shuffling, and splitting into N groups of similar size
N = 5                                   # number of groups, chosen to do 5, so each will have around 14
np.random.seed(42)                      # fixed seed -> same result every run
order = np.random.permutation(len(x))   # random shuffle 
 
predictions = []                        # will hold the N forecasts for 2050
fits = []                              
for k in range(N):
    idx = np.sort(order[k::N])          # every N-th shuffled position = group k
    xs, ys = x[idx], y[idx]             # the years and fertility rates in this group
    slope, intercept = np.polyfit(xs, ys, 1)   # straight-line fit on this group only
    predictions.append(slope * 2050 + intercept)  # prediction for 2050
    fits.append((slope, intercept))
    print(f"Group {k+1}: {len(xs)} points, forecast for 2050 = {predictions[-1]:.3f}")

#this will give all of the groups with the forcast of 2050. 
#these values can then be used to plot

#finding mean and std.

mu = np.mean(predictions)
sigma = np.std(predictions, ddof=1) #divides by N-1. without this 
#this computes sigma = sqr(sum (xi-mu)^2 / (N-1))

print(f"\nResult: {mu:.2f} +- {sigma:.2f} births per woman in 2050")

#imputting the sigma ranges
#1 sigma (68%,)
#2 sigma (95%)
#3 sigma (99.7#)

print(f"1 sigma (68%):   {mu - sigma:.2f} to {mu + sigma:.2f}")
print(f"2 sigma (95%):   {mu - 2*sigma:.2f} to {mu + 2*sigma:.2f}")
print(f"3 sigma (99.7%): {mu - 3*sigma:.2f} to {mu + 3*sigma:.2f}")

#plotting

#scatterplot with extrapolation to 2050, showing the line of best fit,5 lines for the groups, and error bar 2050
plt.figure(figsize=(10,5))
plt.scatter(x, y, s=12, color='grey', label='Data 1950-2023')
years = np.array([1950, 2050])
for s, b in fits:                                   # one blue thin line per group
    plt.plot(years, s * years + b, color='tab:blue', alpha=0.3, lw=1) 
plt.plot(years, slope_all * years + intercept_all, color='tab:red', label='Line of best fit')
plt.errorbar(2050, mu, yerr=sigma, fmt='o', color='black', capsize=4,
             label=f'2050: {mu:.2f} ± {sigma:.2f}')
plt.xlabel('Year')
plt.ylabel('Fertility rate (births per woman)')
plt.title('Graph plotting the line of best fit, 5 subsample groups, and extrapolation to 2050')
plt.grid(True)
plt.legend()
plt.show()


#SAVE FIGURE

g = np.linspace(mu - 4*sigma, mu + 4*sigma, 400)    # x-values for the curve
f = 1/np.sqrt(2*np.pi*sigma**2) * np.exp(-(g - mu)**2 / (2*sigma**2))  # Gaussian formula
plt.plot(g, f, color='black')
shades = {3: '#d6e6f5', 2: '#9cc3e6', 1: '#4f8fc9'}
pcts = {1: '68%', 2: '95%', 3: '99.7%'}
for n in (3, 2, 1):                                 # widest first so narrow ones sit on top
    inside = (g >= mu - n*sigma) & (g <= mu + n*sigma)
    plt.fill_between(g[inside], f[inside], color=shades[n], label=f'{n}σ ({pcts[n]})')
plt.scatter(predictions, np.zeros(N), color='red', zorder=5, label='All 5 Subgroups')
plt.xlabel('Predicted fertility rate in 2050')
plt.ylabel('Probability density')
plt.title('Gaussian distribution from the group forecasts for 2050')
plt.grid(True)
plt.legend()
plt.show()