#!/usr/bin/env python
"""This script contains the utility methods used in the audio_plots file."""

import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import streamlit as st
import glob


@st.cache
def get_dir_overview():
    """
    Adopt this method for the dataset at hand
    :return:
    """
    # find all files
    files = glob.glob("dataset/*.wav")

    # build a label->[sample1, sample2, sample3, ...] mapping
    data = {f'{i}': [] for i in range(50)}
    for sample in files:
        label = sample.split("-")[-1].split(".")[0]
        data[label].append(sample)

    return data


@st.cache
def load_audio_sample(file_path: str):
    y, sr = librosa.load(file_path, sr=22050)
    return y, sr, file_path


def visualization_type_format_func(plot_type: str):

    plot_type_dict = {
        "1": "Wave plot",
        "2": "Linear-scaled Spectrogram",
        "3": "Log-scaled Spectrogram",
        "4": "Mel-scaled Spectrogram",
        "5": "MFCCs",
        "6": "Combined"
    }

    return plot_type_dict.get(plot_type)


def plot_linear_spectrogram(y):
    plt.close('all')
    d = librosa.stft(y)  # STFT of y
    s_db = librosa.amplitude_to_db(np.abs(d), ref=np.max)
    plt.close("all")
    fig, ax = plt.subplots()
    img = librosa.display.specshow(s_db, x_axis='time', y_axis='linear', ax=ax)
    ax.set(title='Linear-scale spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    return plt.gcf()


def plot_log_spectrogram(y):
    plt.close("all")
    fig, ax = plt.subplots()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
    ax.set(title='Log-scale spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    return plt.gcf()


def plot_mel_spectrogram(y, sr):
    plt.close("all")
    fig, ax = plt.subplots()
    m = librosa.feature.melspectrogram(y=y, sr=sr)
    m_db = librosa.power_to_db(m, ref=np.max)
    img = librosa.display.specshow(m_db, y_axis='mel', x_axis='time', ax=ax)
    ax.set(title='Mel-scale spectrograms')
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    return plt.gcf()


def plot_mfccs(y):
    plt.close('all')
    fig, ax = plt.subplots()
    mfccs = librosa.feature.mfcc(y=y, n_mfcc=80)
    img = librosa.display.specshow(mfccs, x_axis='time', ax=ax)
    ax.set(title='MFCCs')
    fig.colorbar(img, ax=ax)

    return plt.gcf()


def plot_wave(y, sr):
    plt.close('all')
    fig, ax = plt.subplots()
    img = librosa.display.waveplot(y, sr=sr, x_axis='time', ax=ax)
    ax.set(title='Waveplot')

    return plt.gcf()

