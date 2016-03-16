import plotly.plotly as py
import plotly.tools as tls
py.sign_in('DorinesRosario', 'ty80gsrxgx')
import plotly.graph_objs as go

data = [
    go.Bar(
        x=['-t 0', '-t 2', '-t 0; -j 0.27', '-t 0; -j 1.9', '-t 0; -j 2.35', '-t 0; -j 2.75', '-t 0; -j 3.6', '-t 2; -j 2.35'],
        y=[-0.00594805686275, 'imp', 'imp', 0.152904834877, 0.15287430796, 0.144602183743, 0.177308230823, 0.15287430796]
    )
]
plot_url = py.plot(data, filename='Global MCC - Single Sequence SVM')