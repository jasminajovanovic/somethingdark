// Store our API endpoint inside queryUrl

// function buildUrl(){
//     const
//         domain = "earthquake.usgs.gov",
//         endpoint = "/fdsnws/event/1/query",
//         format = "geojson",
//         starttime = "2014-01-01",
//         endtime = "2014-01-02",
//         maxLon = -69.52148437,
//         minLon = -123.83789062,
//         maxLat = 48.74894534,
//         minLat = 25.16517337;
//
//     return `https://${domain}${endpoint}?format=${format}&starttime=${starttime}&endtime=${endtime}&maxlongitude=${maxLon}&minlongitude=${minLon}&maxlatitude=${maxLat}&minlatitude=${minLat}`;
// }

Url = 'daly'
// Url_tectonic = 'https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json'

// create radius function
function getRadius(magnitude) {
    return magnitude*25000;
};

function getColor(value) {
   switch (true) {
   case value > 1500:
     return "#ea2c2c";
   case value > 1000:
     return "#ea822c";
   case value > 500:
     return "#ee9c00";
   case value > 300:
     return "#eecc00";
   case value > 100:
     return "#d4ee00";
   default:
     return "#98ee00";
   }
}

function createFeatures(healthData) {
  // console.log(earthquakeData[0]);
  // console.log(tectonicData[0]);
    //
    // var tectonics = L.geoJSON(tectonicData, {
    //   color: "orange",
    // })
    // , {
      // onEachFeature: function(feature, layer) {
      //     layer.bindPopup("<h3>" + feature.properties.place +
      //     "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" + "Magnitude: " + feature.properties.mag);
      //   }
    // })
    function polystyle(feature) {
      return {
          fillColor: getColor(feature.properties.Cardiovascular_diseases),
          weight: 2,
          opacity: 1,
          color: 'white',  //Outline color
          fillOpacity: 0.7
      };
    }

    var health = L.geoJSON(healthData, {




        onEachFeature: function(feature, layer) {
            layer.bindPopup("<h3>" + feature.properties.name + "Cardio: " + feature.properties.Cardiovascular_diseases);
          },

          style: polystyle



        //   pointToLayer: function (feature, latlng) {
        //     return new L.circle(latlng,
        //       {radius: getRadius(feature.properties.mag),
        //       fillColor: getColor(feature.properties.mag),
        //       fillOpacity: 1,
        //       color: "#000",
        //       stroke: true,
        //       weight: .1
        //   })
        // }
        });

    // console.log(`type of tectonics: ${typeof (tectonics)}, type of earthquates: ${typeof (earthquakes)}`);
    myMap = createMap(health);

    var legend = L.control({position: 'bottomright'});

    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
            magnitudes = [0, 1, 2, 3, 4, 5],
            labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < magnitudes.length; i++) {
            div.innerHTML +=
                '<i style="background-color:' + getColor(magnitudes[i] + 1) + '"></i> ' +
                magnitudes[i] + (magnitudes[i + 1] ? '&ndash;' + magnitudes[i + 1] + '<br>' : '+');
        }

        // console.log(div);
        return div;
    };

    // legend.addTo(myMap);
}


function createMap(health) {
    // Define streetmap and darkmap layers
    const lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
            attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
            maxZoom: 18,
            id: "mapbox.light",
            accessToken: API_KEY
    });

    const satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
            attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
            maxZoom: 18,
            id: "mapbox.satellite",
            accessToken: API_KEY
    });

    const outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
            attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
            maxZoom: 18,
            id: "mapbox.outdoors",
            accessToken: API_KEY
    });

    // Define a baseMaps object to hold our base layers
    const baseMaps = {
            "Light Map": lightmap,
            "Satellite": satellite,
            "Outdoors": outdoors
    };

    // Create overlay object to hold our overlay layer
    const overlayMaps = {
            Health: health,
            // Tectonics: tectonics
    };

    // Create our map, giving it the streetmap and earthquakes layers to display on load
    const myMap = L.map("map", {
            center: [37.09, -95.71],
            zoom: 5,
            layers: [lightmap, health]
    });


    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
            collapsed: false
    }).addTo(myMap);

    return myMap
}

(async function(){
    // const queryUrl = buildUrl();
    const healthData = await d3.json(Url);
    // const tectonic = await d3.json(Url_tectonic);
    // Once we get a response, send the data.features object to the createFeatures function
    createFeatures(healthData.features);


    // console.log(tectonic);

})()
