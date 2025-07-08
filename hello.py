import preswald
from preswald import connect, get_df, slider, table, text
import plotly.express as px

# Data
connect()
df = get_df('data/washington_electric_vehicles.csv')

filtered_data = df[(df['City'] == 'Seattle')]

make_histogram = px.histogram(filtered_data, x="Make", title="Manufacturers")
model_bar_graph = px.bar(filtered_data, x="Model", title="Model Names")
year_pie_chart= px.pie(filtered_data, "Model Year", title="Model Year")

# Display
preswald.text("# Electric Vehicle Analysis 🚗")
preswald.text("The following figures highlight various distributions of electric vehicles in Seattle, Washington.")
preswald.text("The data consists of vehicle models from the year 2000 to 2026.")
preswald.text("The table data below has been edited for brevity. The raw data source can be found [here](https://catalog.data.gov/dataset/electric-vehicle-population-data).")

preswald.plotly(make_histogram)
preswald.plotly(model_bar_graph)
preswald.plotly(year_pie_chart)

rows = slider("Rows to Display", min_val=5, default=50)
table(filtered_data[['Make', 'Model', 'Model Year']], limit=rows)
