import streamlit as st

import linear_scale_plots
import log_scale_plots
import mel_scale_plots
import combined_plots
import mfcc_plots
import wave_plots
from audio_loading_utils import get_dir_overview


def visualization_type_format_func(type: str):
    if type == "1":
        return "Waveplots"
    elif type == "2":
        return "Linear-scaled spectrograms"
    elif type == "3":
        return "Log-scaled spectrograms"
    elif type == "4":
        return "Mel-scaled spectrograms"
    elif type == "5":
        return "MFCCs"
    elif type == "6":
        return "Combined"


def main():
    data = get_dir_overview()
    radio1 = st.sidebar.radio(label="Choose visualization type", options=["0", "1", "2", "3", "4", "5", "6"], index=0,
                              format_func=visualization_type_format_func, key="select:vistype",
                              help="Select the visualization type here")

    st.sidebar.markdown("---")

    show_names = st.sidebar.checkbox(label="Show file names", value=False,
                                     help="If checked, shows the name of the processed files below the visualizations")

    if radio1 == "0":
        st.markdown("## Audio feature visualization")
        st.write("<- Select a visualization type in the sidebar")
    elif radio1 == "1":
        wave_plots.build(data, show_names)

    elif radio1 == "2":
        linear_scale_plots.build(data, show_names)

    elif radio1 == "3":
        log_scale_plots.build(data, show_names)

    elif radio1 == "4":
        mel_scale_plots.build(data, show_names)

    elif radio1 == "5":
        mfcc_plots.build(data, show_names)

    elif radio1 == "6":
        combined_plots.build(data)


if __name__ == '__main__':
    st.set_page_config(layout="wide", page_title="Explore audio datasets")
    main()
