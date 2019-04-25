var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 52.515086, lng: 13.418523 },
    zoom: 11
  });

  var sources = ['berlin_atms.json', 'berlin_gas_stations.json', 'berlin_restaurants.json', 'berlin_supermarkets.json', 'berlin_stations.json'];
  var iconBase =
    'http://maps.google.com/mapfiles/kml/shapes/';

  var icons = {
    'berlin_atms.json': {
      icon: iconBase + 'euro.png'
    },
    'berlin_gas_stations.json': {
      icon: iconBase + 'gas_stations.png'
    },
    'berlin_restaurants.json': {
      icon: iconBase + 'dining.png'
    },
    'berlin_supermarkets.json': {
      icon: iconBase + 'grocery.png'
    },
    'berlin_stations.json': {
      icon: iconBase + 'bus.png'
    }
  };

  sources.map(function (source, i) {
    $.getJSON('/static/data/' + source, function (data) {
      console.log(icons[source].icon);
      console.log(icons[source].icon);
      console.log(icons[source].icon);
      markers = data.map(function (item, i) {
        return new google.maps.Marker({
          position: { lat: item.lat, lng: item.lon },
          label: String(item.id),
          icon: icons[source].icon,
        });
      });
      // console.log(markers);
      var markerCluster = new MarkerClusterer(map, markers,
        { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
    });
  });
}
