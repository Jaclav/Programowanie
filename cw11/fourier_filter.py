# %%
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import argparse

#python3 fourier_filter.py --func "exp(-(t-15)**2/0.5)" --f0 0.5 --sigma 0 --duration-time 20
parser = argparse.ArgumentParser()
parser.add_argument("--func", type=str, default="np.sin(2*t) + np.cos(3*t)")
parser.add_argument("--sampling", type=float, default=1000)
parser.add_argument("--duration-time", type=float, default=30)
parser.add_argument("--f0", type=float, default=3)
parser.add_argument("--sigma", type=float, default=0.6)
args = parser.parse_args()

s = args.func
f = eval("lambda t:" + s)
sampling = args.sampling
duration_time = args.duration_time
f0 = args.f0
sigma = args.sigma


def signal_generator(f, sampling, duration_time):
    time_domain = np.linspace(0, duration_time, sampling)
    return [f(t) for t in time_domain]


signal = signal_generator(f, sampling, duration_time)
time_domain = np.linspace(0, duration_time, sampling)
plt.plot(time_domain, signal, label="signal")
plt.legend()
plt.show()


def noise_generator(signal, sigma):
    return signal + np.random.normal(0, sigma, len(signal))


noised = noise_generator(signal, sigma)
plt.plot(time_domain, noised, label="noised")
plt.legend()
plt.show()


def fourier_filter(noised, f0):
    fourier = np.fft.fft(noised)
    time_domain = np.linspace(0, duration_time, sampling)
    frequency_domain = np.fft.fftfreq(len(signal), time_domain[1] - time_domain[0])

    mask = np.abs(frequency_domain) <= f0
    fourier *= mask

    return np.fft.ifft(fourier)


fourier = fourier_filter(noised, f0)
plt.plot(time_domain, fourier, label="denoised")
plt.legend()
plt.show()
