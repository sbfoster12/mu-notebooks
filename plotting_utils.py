import matplotlib.pyplot as plt
import numpy as np

def plot_waveform(ax, waveform):
    ax.plot(waveform.trace)
    ax.set_title(f"CrateNum: {waveform.crateNum}, AMC Slot: {waveform.amcNum}, Channel: {waveform.channelTag}")
    ax.set_xlabel("Clock Tick")
    ax.set_ylabel("ADC Value")



def plot_rf_fit(ax, fitResult):
    #Get the waveform from the fitResult
    waveform = fitResult.waveform.GetObject()
    ax.plot(waveform.trace)
    ax.set_title(f"CrateNum: {waveform.crateNum}, AMC Slot: {waveform.amcNum}, Channel: {waveform.channelTag}")
    ax.set_xlabel("Clock Tick")
    ax.set_ylabel("ADC Value")

    #Get the fit function
    fit_func = fitResult.fitFunc
    print(fit_func)

    # Great fit points
    x_fit = np.linspace(0, len(waveform.trace), 1000)
    # fit_func.SetParameter(0,0.063)
    # fit_func.SetParameter(1,10)
    # fit_func.SetParameter(2,50)
    y_fit = np.array([fit_func.Eval(x) for x in x_fit])

    ax.plot(x_fit, y_fit, 'r-', label='Fit')