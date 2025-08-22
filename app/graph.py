from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x, y, target) -> Chart:
    graph = Chart(
        df, 
        title="Level vs Health by Type"
    ).mark_circle(size=100).encode(
        x="Level:Q",
        y="Health:Q",
        color="Type:N",
        tooltip=Tooltip(["Name", "Type", "Level", "Health"])
    )
    return graph