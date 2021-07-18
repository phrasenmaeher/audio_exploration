import streamlit as st
import os
from audio_loading_utils import load_audio_sample, plot_mfccs, plot_log_spectrogram, plot_mel_spectrogram, \
    plot_linear_spectrogram, plot_wave


def build(data: dict):
    """

    :param data: A dictionary that stores 'class'->'file' mappings
    :return:
    """
    st.markdown("<h1 style='text-align: center; color: black;'>Showing combined plots</h1>",
                unsafe_allow_html=True)

    st.text("")

    col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])

    with col0:

        st.write("Visualization:")
    with col1:
        st.markdown("<h5 style='text-align: center; color: black;'>Wave plot</h5>",
                        unsafe_allow_html=True)
    with col2:
        st.markdown("<h5 style='text-align: center; color: black;'>Linear spectrogram</h5>",
                    unsafe_allow_html=True)
    with col3:
        st.markdown("<h5 style='text-align: center; color: black;'>Log spectrogram</h5>",
                    unsafe_allow_html=True)
    with col4:
        st.markdown("<h5 style='text-align: center; color: black;'>Mel spectrogram</h5>",
                    unsafe_allow_html=True)
    with col5:
        st.markdown("<h5 style='text-align: center; color: black;'>MFCCs</h5>",
                    unsafe_allow_html=True)

    for k, v in data.items():
        col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
        with col0:
            st.text("")
            st.text("")
            st.markdown(f"#### Class {k}")
        with col1:
            y, sr, file_path = load_audio_sample(v[0])
            st.pyplot(plot_wave(y, sr))
        with col2:
            y, sr, file_path = load_audio_sample(v[0])
            st.pyplot(plot_linear_spectrogram(y, sr, file_path))
        with col3:
            y, sr, file_path = load_audio_sample(v[0])
            st.pyplot(plot_log_spectrogram(y))
        with col4:
            y, sr, file_path = load_audio_sample(v[0])
            st.pyplot(plot_mel_spectrogram(y, sr))
        with col5:
            y, sr, file_path = load_audio_sample(v[0])
            st.pyplot(plot_mfccs(y))
