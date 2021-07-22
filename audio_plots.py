#!/usr/bin/env python
"""This script is the audio plots file which contains several audio plots to
graphically display."""

import os
import streamlit as st

from audio_loading_utils import plot_wave, plot_linear_spectrogram, \
    plot_log_spectrogram, plot_mel_spectrogram, plot_mfccs, load_audio_sample


class AudioPlots:
    """AudioPlots plots the specific plot (wave plot, spectrogram, or MFFCs)
       on the open-source, python app Streamlit.

       Attributes:
             sample_data: (dict) consisting of wavefile
             plot_type: (str) defines which type of plot to use
             show_names: (bool) defines whether to show file name.
                        Default: False
    """

    def __init__(self, sample_data, plot_type, show_names=False):
        """Instantiate AudioPlots class with sample data, plot_type,
           and show_names."""
        self.data = sample_data
        self.plot_type = plot_type
        self.show_names = show_names

    def _choose_plot_type(self):

        plot_type_dict = {
            "Wave plot": plot_wave,
            "Linear-scaled Spectrogram": plot_linear_spectrogram,
            "Log-scaled Spectrogram": plot_log_spectrogram,
            "Mel-scaled Spectrogram": plot_mel_spectrogram,
            "MFCCs": plot_mfccs
        }
        return plot_type_dict.get(self.plot_type)

    def _plot(self, sample_value, sample_func):
        y, sr, file_path = load_audio_sample(sample_value)
        if self.show_names:
            st.markdown(f"<h5 style='text-align: center; color: black;'>"
                        f"{os.path.basename(file_path)}</h5>",
                        unsafe_allow_html=True)

        if self.plot_type in ["Wave plot", "Mel-scaled Spectrogram"]:
            st.pyplot(sample_func(y, sr))
        else:
            st.pyplot(sample_func(y))

    def build_non_combined(self):
        """Builds the specific plot for each sample dataset."""

        if self.plot_type in ["Linear-scaled Spectrogram", "Log-scaled Spectrogram",
                              "Mel-scaled Spectrogram"]:
            st.markdown(f"<h1 style='text-align: center; color: black;'>"
                        f"Showing {self.plot_type}s</h1>",
                        unsafe_allow_html=True)
        elif self.plot_type == "Wave plot":
            st.markdown(f"<h1 style='text-align: center; color: black;'>"
                        f"Showing {self.plot_type}s</h1>",
                        unsafe_allow_html=True)
        else:
            st.markdown(f"<h1 style='text-align: center; color: black;'>"
                        f"Showing {self.plot_type} plots</h1>",
                        unsafe_allow_html=True)
        st.text("")

        plt_func = self._choose_plot_type()

        for k, v in self.data.items():
            col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
            with col0:
                st.text("")
                st.text("")
                st.markdown(f"#### Class {k}")
            with col1:
                self._plot(v[0], plt_func)
            with col2:
                self._plot(v[1], plt_func)
            with col3:
                self._plot(v[2], plt_func)
            with col4:
                self._plot(v[3], plt_func)
            with col5:
                self._plot(v[4], plt_func)

    def build_combined(self):
        """Builds all the plots for each sample dataset."""

        st.markdown("<h1 style='text-align: center; color: black;'>"
                    "Showing combined plots</h1>",
                    unsafe_allow_html=True)

        st.text("")

        col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])

        with col0:
            st.write("Visualization:")
        with col1:
            st.markdown("<h5 style='text-align: center; color: black;'>"
                        "Wave plot</h5>",
                        unsafe_allow_html=True)
        with col2:
            st.markdown("<h5 style='text-align: center; color: black;'>"
                        "Linear Spectrogram</h5>",
                        unsafe_allow_html=True)
        with col3:
            st.markdown("<h5 style='text-align: center; color: black;'>"
                        "Log Spectrogram</h5>",
                        unsafe_allow_html=True)
        with col4:
            st.markdown("<h5 style='text-align: center; color: black;'>"
                        "Mel Spectrogram</h5>",
                        unsafe_allow_html=True)
        with col5:
            st.markdown("<h5 style='text-align: center; color: black;'>"
                        "MFCCs</h5>",
                        unsafe_allow_html=True)

        for k, v in self.data.items():
            col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
            with col0:
                st.text("")
                st.text("")
                st.markdown(f"#### Class {k}")
            with col1:
                self.plot_type = "Wave plot"
                self._plot(v[0], plot_wave)
            with col2:
                self.plot_type = "Linear-scaled Spectrogram"
                self._plot(v[0], plot_linear_spectrogram)
            with col3:
                self.plot_type = "Log-scaled Spectrogram"
                self._plot(v[0], plot_log_spectrogram)
            with col4:
                self.plot_type = "Mel-scaled Spectrogram"
                self._plot(v[0], plot_mel_spectrogram)
            with col5:
                self.plot_type = "MFCCs"
                self._plot(v[0], plot_mfccs)

    def run_build(self):
        self.build_combined() if self.plot_type == "Combined" \
            else self.build_non_combined()
