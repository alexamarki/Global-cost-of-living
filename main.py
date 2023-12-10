import folium
from folium.plugins import MarkerCluster


def mapper(lowerb, higherb, metric, df_, gj):
    df = df_[[metric, 'country', 'city', 'coord']]
    df = df[(df[metric] >= int(lowerb)) & (df[metric] <= int(higherb))]
    print(df)
    df = df.dropna()
    countries = df.country.unique()
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=3, max_bounds=True)
    clusters = {}
    for i in countries:
        marker_cluster = MarkerCluster(
            name=i,
            overlay=True,
            control=True,
        )
        clusters[i] = marker_cluster
        clusters[i].add_to(m)

    for index, row in df.iterrows():
        x, y = map(float, row['coord'].split())
        city = folium.Marker([y, x], popup=f"{row['country']}, {row['city']}").add_to(m)
        clusters[row['country']].add_child(city)

    folium.Choropleth(
        geo_data=gj,
        name='choropleth',
        data=df,
        columns=['country', metric],
        key_on='properties.ADMIN',
        fill_color='YlGn',
        nan_fill_color='gray',
        fill_opacity=0.6,
        line_opacity=0.2
    ).add_to(m)
    folium.TileLayer('cartodbpositron').add_to(m)
    m
    map_html = m._repr_html_()
    return map_html
