# stockPlot
setup:

1. clone this locally
2. In the terminal; execute: pip install streamlit --upgrade
> note: dependencies tba in requirements.txt so that pip install can be executed in one command. for now, please manually pip install the libraries this app uses: bokeh, plotly, seahorn
3. then, do: streamlit run 1_Overview.py
4. see if you get something like this
   ![image](https://github.com/EmilieYZhang/stockPlot/assets/68432655/3377d7dc-ab5f-4648-b82b-8216e1aaf9bc)

>Note:
>you have many options as tools to plot stuff: 1. plotly tried a 3D model with this
https://plotly.com/python/3d-charts/
>or 2. Bokeh which is what i have been using mostly
https://docs.bokeh.org/en/latest/docs/gallery.html
>or any other python plotting library: matplotlib, seaborn, etc.

& yes, our frontend which uses streamlit is seamless an can accept plots from most libraries to display

>important: python parsing should be done dynamically, no hard coding in this repo
