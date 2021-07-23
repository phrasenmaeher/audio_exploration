#!/usr/bin/env python
"""This script is the audio plots file which contains several audio plots to
graphically display."""

import os
import streamlit as st

from audio_loading_utils import load_audio_sample, DisplayPlots


class AudioPlots:
    """AudioPlots plots the specific plot (wave plot, spectrogram, or MFFCs)
       on the open-source, python app Streamlit.

       Attributes:
             sample_data: (dict) consisting of wave files
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

    def _plot(self, sample_value):
        """Plots the audio time series based on type of plot specified.

           Args:
               sample_value: (str) path where wave file is located
        """

        audio_time_series, sample_rate, file_path = load_audio_sample(sample_value)

        if self.show_names:
            st.markdown(f"<h5 style='text-align: center; color: black;'>"
                        f"{os.path.basename(file_path)}</h5>",
                        unsafe_allow_html=True)

        st.pyplot(DisplayPlots(audio_time_series, sample_rate,
                               plot_type=self.plot_type).display())

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

        for key, value in self.data.items():
            col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
            with col0:
                st.text("")
                st.text("")
                st.markdown(f"#### Class {key}")
            with col1:
                self._plot(value[0])
            with col2:
                self._plot(value[1])
            with col3:
                self._plot(value[2])
            with col4:
                self._plot(value[3])
            with col5:
                self._plot(value[4])

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

        for key, value in self.data.items():
            col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
            with col0:
                st.text("")
                st.text("")
                st.markdown(f"#### Class {key}")
            with col1:
                self.plot_type = "Wave plot"
                self._plot(value[0])
            with col2:
                self.plot_type = "Linear-scaled Spectrogram"
                self._plot(value[0])
            with col3:
                self.plot_type = "Log-scaled Spectrogram"
                self._plot(value[0])
            with col4:
                self.plot_type = "Mel-scaled Spectrogram"
                self._plot(value[0])
            with col5:
                self.plot_type = "MFCCs"
                self._plot(value[0])

    def run_build(self):
        """Runs the builds based on whether the option is
           Combined or not combined."""

        return self.build_combined() if self.plot_type == "Combined" \
            else self.build_non_combined()
