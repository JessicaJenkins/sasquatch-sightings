"use strict";

function initMap() {

  const mapCenter = { lat: 37.601773, lng: -122.202870 };

  // debugger

  const map = new google.maps.Map(document.getElementById('map'), {
    center: mapCenter,
    // scrollwheel: false,
    zoom: 10,
    // zoomControl: true,
    // panControl: false,
    // streetViewControl: false,
    // mapTypeId: google.maps.MapTypeId.TERRAIN
  });

  // const infoWindow = new google.maps.InfoWindow();

  // $.get('/api/sasquatch', (sightings) => {
  //   for (let sighting of sightings) {
  //     const marker = new google.maps.Marker({
  //       position: new google.maps.LatLng(sighting.lat, sighting.lng),
  //       map: map,
  //     })
  //   }
  // })
};
