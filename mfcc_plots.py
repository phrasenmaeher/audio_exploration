import streamlit as st
import os
from audio_loading_utils import load_audio_sample, plot_mfccs


def build(data: dict, show_names: bool = False):
    """

    :param data: A dictionary that stores 'class'->'file' mappings
    :return:
    """

    st.markdown("<h1 style='text-align: center; color: black;'>Showing MFCCs plots</h1>",
                unsafe_allow_html=True)
    st.text("")

    for k, v in data.items():
        col0, col1, col2, col3, col4, col5 = st.beta_columns([1, 2, 2, 2, 2, 2])
        with col0:
            st.text("")
            st.text("")
            st.markdown(f"#### Class {k}")
        with col1:
            y, sr, file_path = load_audio_sample(v[0])
            if show_names:
                st.markdown(f"<h5 style='text-align: center; color: black;'>{os.path.basename(file_path)}</h5>",
                            unsafe_allow_html=True)
            st.pyplot(plot_mfccs(y))
        with col2:
            y, sr, file_path = load_audio_sample(v[1])
            if show_names:
                st.markdown(f"<h5 style='text-align: center; color: black;'>{os.path.basename(file_path)}</h5>",
                            unsafe_allow_html=True)
            st.pyplot(plot_mfccs(y))
        with col3:
            y, sr, file_path = load_audio_sample(v[2])
            if show_names:
                st.markdown(f"<h5 style='text-align: center; color: black;'>{os.path.basename(file_path)}</h5>",
                            unsafe_allow_html=True)
            st.pyplot(plot_mfccs(y))
        with col4:
            y, sr, file_path = load_audio_sample(v[3])
            if show_names:
                st.markdown(f"<h5 style='text-align: center; color: black;'>{os.path.basename(file_path)}</h5>",
                            unsafe_allow_html=True)
            st.pyplot(plot_mfccs(y))
        with col5:
            y, sr, file_path = load_audio_sample(v[4])
            if show_names:
                st.markdown(f"<h5 style='text-align: center; color: black;'>{os.path.basename(file_path)}</h5>",
                            unsafe_allow_html=True)
            st.pyplot(plot_mfccs(y))
