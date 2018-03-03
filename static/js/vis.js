var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 11,
    center: {lng:-84.3880 , lat: 33.7490},
    mapTypeId: 'terrain'
  });

  // Create a <script> tag and set the USGS URL as the source.
  // var script = document.createElement('script');

  // JSON OBJECT FROM HARDWARE
  // script.src = 'https://developers.google.com/maps/documentation/javascript/examples/json/earthquake_GeoJSONP.js';
  // document.getElementsByTagName('head')[0].appendChild(script);

  var results = {{ data | tojson}};

  var heatmapData = [];

  for (var i = 0; i < results.length; i++) {

    var latLng = new google.maps.LatLng(results[i].location[0], results[i].location[1])''
    var magnitude = results[i].activity_v;

    var weightedLoc = {
      location : latLng,
      weight : magnitude
    };
    heatmapData.push(weightedLoc);
  }
  var heatmap = new google.maps.visualization.HeatmapLayer({
    data:heatmapData,
    dissipating:false,
    map: map
  });


}

function eqfeed_callback(results) {
  var heatmapData = [];
  for (var i = 0; i &lt; results.features.length; i++) {
    var coords = results.features[i].geometry.coordinates;
    var latLng = new google.maps.LatLng(coords[1], coords[0]);
    var magnitude = results.features[i].properties.mag;
    var weightedLoc = {
      location: latLng,
      weight: Math.pow(2, magnitude)
    };
    heatmapData.push(weightedLoc);
  }
  var heatmap = new google.maps.visualization.HeatmapLayer({
    data: heatmapData,
    dissipating: false,
    map: map
  });
}





function eqfeed_callback(results) {
  console.log('callback');
  var heatmapData = [];
  for (var i = 0; i < results.features.length; i++) {
    var coords = results.features[i].geometry.coordinates;
    var latLng = new google.maps.LatLng(coords[1], coords[0]);
    heatmapData.push(latLng);
  }
  var heatmap = new google.maps.visualization.HeatmapLayer({
    data: heatmapData,
    dissipating: false,
    map: map
  });
}