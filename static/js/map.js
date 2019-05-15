"use strict";

let centerMapLat = 46.383744
let centerMapLng = -122.278250

function initMap() {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: centerMapLat, lng: centerMapLng},
    zoom: 10
  });

  const infoWindow = new google.maps.InfoWindow();

  $.get('/api/sightings', (sightings) => {

    const markers = []
    
    for (let sighting of sightings) {
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(sighting.sightingLat, sighting.sightingLng),
        map: map,
        icon: {
          url: '/static/img/white-marker.png',
          scaledSize: new google.maps.Size(50, 50)
        }
      });

      markers.push(marker);

      // Define the content of the infoWindow
      const html = `<div class="window-content">
        <div class="sasquatch-thumbnail">
          <img
            src="/static/img/FILL_THIS_IN"
            alt="sasquatch"
          >
        </div>
        <ul class="sighting-info">
          <li><b>Date: </b>${sighting.sightingDate}</li>
          <li><b>Description: </b><a href = '/sighting/${sighting.sightingId}'>
          Sighting description</a>
          </li>
        </ul>
      </div>`;

      google.maps.event.addListener(marker, 'click', () => {
        infoWindow.close();
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
      });
    }
  var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
  });
}