import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Dashboard Theme
# ==========================================================

CHART_HEIGHT = 450


# ==========================================================
# BAR CHART
# ==========================================================

def bar_chart(
    df,
    x,
    y,
    title,
    color=None,
    horizontal=False
):

    if horizontal:

        fig = px.bar(
            df,
            x=y,
            y=x,
            color=color,
            orientation="h",
            text=y,
            title=title,
            height=CHART_HEIGHT
        )

    else:

        fig = px.bar(
            df,
            x=x,
            y=y,
            color=color,
            text=y,
            title=title,
            height=CHART_HEIGHT
        )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title()
    )

    fig.update_traces(textposition="outside")

    return fig


# ==========================================================
# PIE CHART
# ==========================================================

def pie_chart(
    df,
    names,
    values,
    title
):

    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=0.45,
        title=title,
        height=CHART_HEIGHT
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    fig.update_traces(textposition="inside")

    return fig


# ==========================================================
# DONUT CHART
# ==========================================================

def donut_chart(
    df,
    names,
    values,
    title
):

    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=0.6,
        title=title,
        height=CHART_HEIGHT
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


# ==========================================================
# HISTOGRAM
# ==========================================================

def histogram(
    df,
    column,
    title,
    bins=15
):

    fig = px.histogram(
        df,
        x=column,
        nbins=bins,
        title=title,
        height=CHART_HEIGHT
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


# ==========================================================
# SCATTER
# ==========================================================

def scatter_chart(
    df,
    x,
    y,
    color=None,
    title=""
):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        size_max=12,
        title=title,
        height=CHART_HEIGHT
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


# ==========================================================
# LINE CHART
# ==========================================================

def line_chart(
    df,
    x,
    y,
    title
):

    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=title,
        height=CHART_HEIGHT
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig


# ==========================================================
# MAP
# ==========================================================

def map_chart(df):

    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lng",
        hover_name="first_name",
        hover_data=["city", "country"],
        zoom=1,
        height=600
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=40, b=0)
    )

    return fig


# ==========================================================
# KPI INDICATOR
# ==========================================================

def indicator(title, value):

    fig = go.Figure()

    fig.add_trace(

        go.Indicator(

            mode="number",

            value=value,

            title={"text": title}

        )

    )

    fig.update_layout(height=180)

    return fig


# ==========================================================
# GAUGE CHART
# ==========================================================

def gauge_chart(value, title, maximum):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            title={"text": title},

            gauge={

                "axis": {"range": [0, maximum]}

            }

        )

    )

    fig.update_layout(height=300)

    return fig


# ==========================================================
# TABLE
# ==========================================================

def data_table(df):

    fig = go.Figure(

        data=[

            go.Table(

                header=dict(

                    values=list(df.columns),

                    fill_color="royalblue",

                    font=dict(color="white", size=13)

                ),

                cells=dict(

                    values=[df[col] for col in df.columns]

                )

            )

        ]

    )

    return fig