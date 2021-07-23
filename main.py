#!/usr/bin/env python
"""This script is the main driver file."""

import streamlit as st

from audio_loading_utils import get_dir_overview, \
    visualization_type_format_func
from audio_plots import AudioPlots


def main():
    data = get_dir_overview()

    radio1 = st.sidebar.radio(label="Choose visualization type",

                              options=[str(i) for i in range(7)], index=0,

                              format_func=visualization_type_format_func,
                              key="select:vistype",
                              help="Select the visualization type here")

    st.sidebar.markdown("---")

    bool_show_names = st.sidebar.checkbox(label="Show file names", value=False,
                                          help="If checked, shows the name of "
                                               "the processed files above the "
                                               "visualizations")

    if radio1 == "0":
        st.markdown("## Audio feature visualization")
        st.write("<- Select a visualization type in the sidebar")
    else:
        audio_plot_type = visualization_type_format_func(radio1)
        AudioPlots(data, audio_plot_type,
                   show_names=bool_show_names).run_build()


if __name__ == '__main__':
    st.set_page_config(layout="wide", page_title="Explore audio datasets")
    main()
