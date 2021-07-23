#!/usr/bin/env python
"""This script contains the utility methods used in the audio_plots file."""

import glob
import librosa
import librosa.display

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


@st.cache
def get_dir_overview():
    """Adopt this method for the dataset at hand."""
    # find all files
    files = glob.glob("dataset/*.wav")

    # build a label->[sample1, sample2, sample3, ...] mapping
    data = {f'{i}': [] for i in range(50)}
    for sample in files:
        label = sample.split("-")[-1].split(".")[0]
        data[label].append(sample)

    return data


@st.cache
def load_audio_sample(file_path, sample_rate=22050):
    """Loads the wave file.

       Args:
           file_path: (str) path where wave file is located
           sample_rate: (int) sample rate of file. Default: 22050 seconds

       Returns:
           signal_data: (nd.array) time series data
           sampling_rate: (int) sampling rate of signal_data
           file_path: (str) path where wave file is located
    """
    signal_data, sampling_rate = librosa.load(file_path, sr=sample_rate)
    return signal_data, sampling_rate, file_path


def visualization_type_format_func(plot_type):
    """Retrieves the name of the plot used, labelled from 1-6.

       Args:
           plot_type: (str) integer (saved as a string) corresponding
                      to the specific plot type
    """

    plot_type_dict = {
        "1": "Wave plot",
        "2": "Linear-scaled Spectrogram",
        "3": "Log-scaled Spectrogram",
        "4": "Mel-scaled Spectrogram",
        "5": "MFCCs",
        "6": "Combined"
    }
    return plot_type_dict.get(plot_type)


class DisplayPlots:
    """DisplayPlots serves to create the specific plot
       (wave plot, spectrogram, or MFFCs).

       Attributes:
             data: (nd.array) time series data
             signal_sample_rate: (int) sampling rate of data
             plot_type: (bool) defines which plot to use. Default: None

       Raises:
           ValueError: if plot_type is None.
    """

    def __init__(self, data, signal_sample_rate, plot_type=None):
        """Instantiate DisplayPlots class with data, signal_sample_rate,
           plot_type."""

        self.data = data
        self.signal_sample_rate = signal_sample_rate
        self.plot_type = plot_type

        if self.plot_type is None:
            raise ValueError("Error! Plot type cannot be None.")

    def _choose_plot_type(self):
        """Retrieves the plot function to be used."""

        plot_type_dict = {
            "Wave plot": self.get_wave,
            "Linear-scaled Spectrogram": self.get_linear_or_log_spectrogram,
            "Log-scaled Spectrogram": self.get_linear_or_log_spectrogram,
            "Mel-scaled Spectrogram": self.get_mel_spectrogram,
            "MFCCs": self.get_mfccs
        }
        return plot_type_dict.get(self.plot_type)

    def get_wave(self, sample_ax):
        """Gets the wave plot.

           Args:
               sample_ax: (object) sample axes used from matplotlib library

            Returns:
                wave plot
        """
        img = librosa.display.waveplot(self.data,
                                       sr=self.signal_sample_rate,
                                       x_axis='time',
                                       ax=sample_ax)
        sample_ax.set(title=self.plot_type)
        return plt.gcf()

    def get_linear_or_log_spectrogram(self):
        """Gets either the linear or log Spectrogram."""
        return librosa.amplitude_to_db(np.abs(librosa.stft(self.data)),
                                       ref=np.max)

    def get_mel_spectrogram(self):
        """Gets the mel spectrogram."""
        return librosa.power_to_db(librosa.feature.melspectrogram(y=self.data,
                                                                  sr=self.signal_sample_rate),
                                   ref=np.max)

    def get_mfccs(self, number_of_mfccs=80):
        """Gets the mel-frequency cepstrum coefficients.

           Args:
               number_of_mfccs: (int) number of MFCCs to use. Default: 80
        """
        return librosa.feature.mfcc(y=self.data,
                                    n_mfcc=number_of_mfccs)

    def _set_specshow(self, sample_ax, sample_fig, *args):

        mini_plot_dict = {
            "Linear-scaled Spectrogram": "linear",
            "Log-scaled Spectrogram": "log",
            "Mel-scaled Spectrogram": "mel",
        }

        if mini_plot_dict.get(self.plot_type) is not None:
            img = librosa.display.specshow(np.array(args),
                                           x_axis="time",
                                           y_axis=mini_plot_dict.get(self.plot_type),
                                           ax=sample_ax)
            sample_fig.colorbar(img, ax=sample_ax, format="%+2.f dB")
        else:
            img = librosa.display.specshow(np.array(args),
                                           x_axis="time",
                                           ax=sample_ax)
            sample_fig.colorbar(img, ax=sample_ax)

        sample_ax.set(title=self.plot_type)
        return plt.gcf()

    def display(self):
        """Displays the specific plot."""

        plt.close("all")
        fig, axes = plt.subplots()

        func = self._choose_plot_type()

        if self.plot_type != "Wave plot":
            *args, = func()
            return self._set_specshow(axes, fig, *args)
        return func(axes)
