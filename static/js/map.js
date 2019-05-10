"use strict";

function initMap() {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 35.3011, lng: -99.1702},
    zoom: 10
  });

  const infoWindow = new google.maps.InfoWindow();

  $.get('/api/sightings', (sightings) => {
    
    for (let sighting of sightings) {
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(sighting.lat, sighting.lng),
        map: map,
        icon: {
          url: '/static/img/white-marker.png',
          scaledSize: new google.maps.Size(50, 50)
        }
      });  

      // Define the content of the infoWindow
      const html = `<div class="window-content">
        <div class="sasquatch-thumbnail">
          <img
            src="/static/img/FILL_THIS_IN"
            alt="sasquatch"
          >
        </div>
        <ul class="sighting-info">
          <li><b>Date: </b>${sighting.date}</li>
          <li><b>Description: </b>LINK HERE</li>
        </ul>
      </div>`;

      google.maps.event.addListener(marker, 'click', () => {
        infoWindow.close();
        infoWindow.setContent(html);
        infoWindow.open(map, marker);
      });
    }
  });
}