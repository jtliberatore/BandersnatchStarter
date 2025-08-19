from altair import Chart


def chart(df, x, y, target) -> Chart:
    

    graph = (
        Chart(
            df,
            title=f"{y} by {x} for {target}",
        )
        .mark_circle(size=100)
        .encode(
            x=x,
            y=y,
            color=target,
            tooltip=list(df.columns),
        )
        .configure_axis(
            labelFontSize=12,
            titleFontSize=14,
        )
        .configure_view(
            strokeWidth=0,
        )
    )

    return graph

