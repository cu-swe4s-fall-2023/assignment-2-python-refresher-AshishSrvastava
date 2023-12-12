import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load data
north_american_df = pd.read_csv("merged_data.csv")

# Color map for countries
colors = {
    "United States of America": "xkcd:pastel blue",
    "Mexico": "xkcd:yellowish green",
    "Canada": "xkcd:pink",
    "Guatemala": "orange",
}

# Create a 2x2 subplot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# Top Left (A): Line plot of Year vs Average Temperature
for country, color in colors.items():
    country_data = north_american_df[north_american_df["Area"] == country]
    ax1.plot(
        country_data["Year"],
        country_data["Average Temperature °C"],
        label=country,
        color=color,
    )
ax1.set_xlabel("Year")
ax1.set_ylabel("Average Temperature (°C)")
ax1.set_title("A: Year vs Average Temperature")
ax1.legend()
ax1.grid(True)

# Top Right (B): Scatter plot of year vs total emissions
for country, color in colors.items():
    country_data = north_american_df[north_american_df["Area"] == country]
    ax2.scatter(
        country_data["Year"],
        country_data["total_emission"],
        label=country,
        color=color,
    )
ax2.set_xlabel("Year")
ax2.set_ylabel("Total Emissions (kt CO$_2$)")
ax2.set_title("B: Year vs Total CO$_2$ Emissions")
ax2.legend()

# Bottom Left (C): Scatter plot of GDP vs Total emissions
years = north_american_df["Year"].unique()
years.sort()  # Sort years to align with the colormap
norm = plt.Normalize(years.min(), years.max())
sm = plt.cm.ScalarMappable(cmap="viridis", norm=norm)
sm.set_array([])
scatter = ax3.scatter(
    north_american_df["GDP"],
    north_american_df["total_emission"],
    c=north_american_df["Year"],
    cmap="viridis",
    alpha=0.6,
    edgecolors="w",
)
ax3.set_xlabel("GDP")
ax3.set_ylabel("Total Emissions")
ax3.set_title("C: GDP vs Total Emissions Colored by Year")
fig.colorbar(sm, ax=ax3, label="Year")

# Bottom Right (D): Bar Chart of Average GDP vs Average Total Emissions for Each Country
average_data = north_american_df.groupby("Area")[
    ["GDP", "total_emission"]
].mean()

# Plotting GDP bars on ax4
ax4.set_xlabel("Country")
ax4.set_ylabel("Average GDP")
for country in average_data.index:
    ax4.bar(
        country,
        average_data.loc[country, "GDP"],
        color=colors.get(country, "grey"),
        alpha=0.6,
    )

# Adding second axis for total emissions line plot
ax4_2 = ax4.twinx()
ax4_2.set_ylabel("Average Total Emissions", color="tab:red")
ax4_2.plot(
    average_data.index,
    average_data["total_emission"],
    color="tab:red",
    marker="o",
    label="Average Total Emissions (kt CO$_2$)",
)
ax4_2.tick_params(axis="y", labelcolor="tab:red")

ax4.set_title("D: Average GDP vs Average Total Emissions")

# Make all spines invisible
# ax1, Top Left Panel
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# ax2, Top Right Panel
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# ax3, Bottom Left Panel
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)

# ax4, Bottom Right Panel - Primary Axis
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)

# ax4_2, Bottom Right Panel - Secondary Axis (necessary?)
ax4_2.spines["top"].set_visible(False)
ax4_2.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("four_panel_plot.png")
