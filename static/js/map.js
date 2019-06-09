"use strict";

let centerMapLat = 46.383744
let centerMapLng = -122.278250

function initMap() {
  const map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: centerMapLat, lng: centerMapLng},
    zoom: 10,
    streetViewControl: false,
    mapTypeControl: false,
    fullscreenControl: false,
    zoomControl: true,
    zoomControlOptions: {
        position: google.maps.ControlPosition.TOP_RIGHT
    },
    styles: [
  {
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#212121"
      }
    ]
  },
  {
    "elementType": "labels.icon",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#212121"
      }
    ]
  },
  {
    "featureType": "administrative",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "featureType": "administrative.country",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#9e9e9e"
      }
    ]
  },
  {
    "featureType": "administrative.land_parcel",
    "stylers": [
      {
        "visibility": "off"
      }
    ]
  },
  {
    "featureType": "administrative.locality",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#bdbdbd"
      }
    ]
  },
  {
    "featureType": "landscape.natural.terrain",
    "stylers": [
      {
        "color": "#39393a"
      },
      {
        "visibility": "simplified"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#181818"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#616161"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#1b1b1b"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry.fill",
    "stylers": [
      {
        "color": "#2c2c2c"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#8a8a8a"
      }
    ]
  },
  {
    "featureType": "road.arterial",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#373737"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#3c3c3c"
      }
    ]
  },
  {
    "featureType": "road.highway.controlled_access",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#4e4e4e"
      }
    ]
  },
  {
    "featureType": "road.local",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#616161"
      }
    ]
  },
  {
    "featureType": "transit",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#757575"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#000000"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#3d3d3d"
      }
    ]
  }
]
  });

  const infoWindow = new google.maps.InfoWindow();

  $.get('/api/sightings', (sightings) => {

    const markers = []
    
    for (let sighting of sightings) {
      const marker = new google.maps.Marker({
        position: new google.maps.LatLng(sighting.sightingLat, sighting.sightingLng),
        map: map,
        icon: {
          url: '/static/images/white-marker.png',
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

  // Edit imagePath after final bigfoot 'foot' is added to images folder

  const markerCluster = new MarkerClusterer(map, markers,
    {imagePath: 'static/images/white-marker'});

  });
}