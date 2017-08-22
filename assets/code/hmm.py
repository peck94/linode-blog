import hmmlearn.hmm as hmm
import warnings
import matplotlib.pyplot as plt
import numpy as np

# load the data
print('Loading data...')
series = []
with open('../files/ibm.csv', 'r') as file:
    for i, line in enumerate(file):
        if i > 0:
            parts = line.split(',')
            if len(parts) == 2:
                stock = float(parts[1])
                series.append([stock])
print('Loaded {} samples.'.format(len(series)))

# construct the model
model = hmm.GaussianHMM(n_components=3, covariance_type="full", n_iter=1000)

# fit the model
print('Fitting model...')
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    model.fit(series)

# detect anomalies in the time series
states = []
with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    states = model.predict(series)

anomalies = []
for i in range(len(series)-1):
    if states[i+1] != states[i]:
        anomalies.append(i+1)

print('Anomalies: {}'.format(anomalies))
print('Model means: {}'.format(model.means_))
print('Model covariances: {}'.format(model.covars_))
print('Initial probabilities: {}'.format(model.startprob_))
print('Transition matrix: {}'.format(np.round(model.transmat_, 2)))

plt.plot(series)
plt.title('IBM common stock closing prices 1962-1965')
plt.xlabel('time')
plt.ylabel('stock')
for anomaly in anomalies:
    plt.axvline(anomaly, color='r')
plt.show()
