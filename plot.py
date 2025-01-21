import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import time

class GPSPlotter:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 5))
        self.ax = plt.axes(projection=ccrs.PlateCarree())

        # [lon_min, lon_max, lat_min, lat_max]
        # self.ax.set_extent([140, 154, -40, -28], crs=ccrs.PlateCarree()) # MGA2020 Zone 56
        self.ax.set_extent([151.2, 151.3, -33.95, -33.9], crs=ccrs.PlateCarree()) # Test area

        # # Add features to the map within the specified extent
        # self.ax.add_feature(cfeature.LAND, edgecolor='black')
        # self.ax.add_feature(cfeature.OCEAN)
        # self.ax.add_feature(cfeature.COASTLINE)
        # self.ax.add_feature(cfeature.BORDERS, linestyle=':')

        # Add gridlines
        self.ax.gridlines(draw_labels=True)

        # Track the last plotted coordinate
        self.last_lon, self.last_lat = None, None

    def update_plot(self, lon, lat):
        if self.last_lon is not None and self.last_lat is not None:
            self.ax.plot([self.last_lon, lon], [self.last_lat, lat], color='red', transform=ccrs.Geodetic())
        self.ax.plot(lon, lat, marker='o', color='red', markersize=5, transform=ccrs.Geodetic())
        self.last_lon, self.last_lat = lon, lat

        plt.draw()
        plt.pause(0.1)

    def plot(self, data):
        try:
            lon, lat = map(float, data.split(',')[4:6])
            self.update_plot(lon, lat)
        except ValueError:
            print(f"Invalid data: {data}")

if __name__ == "__main__":
    plotter = GPSPlotter()
    plotter.test_input()
    plt.show()