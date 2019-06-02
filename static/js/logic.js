// Creating map object
var myMap = L.map("map", {
    center: [40.7128, -74.0059],
    zoom: 2
});

var filterDict = {'Cardiovascular_diseases':0, 'Diabetes_mellitus':0,
                  "Malignant_neoplasms" :0, "Respiratory_diseases": 0,
                  "Infectious_and_parasitic_diseases":0, "Respiratory_Infectious":0}

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
}).addTo(myMap);

function round(value, precision) {
    var multiplier = Math.pow(10, precision || 0);
    return Math.round(value * multiplier) / multiplier;
}

function diseaseSum (dictionary, feature) {
  var mySum = 0
  for (var key in dictionary) {
    if (dictionary[key]) {
      mySum += feature.properties[`${key}`]
    }
  }
  return round(mySum, 2)
}
function itemsChecked (dictionary) {
  for (var key in dictionary) {
    if (dictionary[key]) {
      console.log(`${key} is checked`);
      return 1
    }
  }
  console.log("nothing is checked");
  return 0
}
function drawMap(data) {

  var geojson = L.choropleth(data, {
      valueProperty: function (feature) {
        return diseaseSum(filterDict, feature)
      },
      scale: ['white', 'red'],
      steps: 50,
      mode: 'q',
      style: {
          color: '#fff',
          weight: 1,
          fillOpacity: 0.8
      },

      // Binding a pop-up
      onEachFeature: function(feature, layer) {
          layer.bindPopup("<h2>" + feature.properties.name + "<\h2><h3> Value: " + diseaseSum(filterDict, feature) + "<\h3>");
        },
  }).addTo(myMap);
}

(async function(){
    // Link to GeoJSON
    var myChoro = null;
    const APILink = "/daly";
    // Grab data with D3
    data = await d3.json(APILink)
    drawMap(data)
    // create the control

    var choices = L.control({position: 'topleft'});

    choices.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info');
        div.innerHTML = '<h3>Non Communicable Diseases</h3><form> \
                              <input id="Cardiovascular_diseases" type="checkbox"/>Cardiovascular Diseases<br>\
                              <input id="Malignant_neoplasms" type="checkbox"/>Cancer<br>\
                              <input id="Diabetes_mellitus" type="checkbox"/>Diabetes<br>\
                              <input id="Respiratory_diseases" type="checkbox"/>Respiratory Diseases<br>\
                          <h3>Communicable Diseases</h3> \
                              <input id="Infectious_and_parasitic_diseases" type="checkbox"/>Infectious and Parasitic Diseases<br>\
                              <input id="Respiratory_Infectious" type="checkbox"/>Infectious Respiratory Diseases<br>\
                          </form>';

        return div;
    };
    choices.addTo(myMap);

    // add the event handler
    function handleCommand() {
      if (this.checked) {
        filterDict[this.id] = 1
      }
      else {
        filterDict[this.id] = 0
      }
       drawMap(data)
    }

    document.getElementById("Cardiovascular_diseases").addEventListener("click", handleCommand, false);
    document.getElementById("Malignant_neoplasms").addEventListener("click", handleCommand, false);
    document.getElementById("Diabetes_mellitus").addEventListener("click", handleCommand, false);
    document.getElementById("Respiratory_diseases").addEventListener("click", handleCommand, false);
    document.getElementById("Infectious_and_parasitic_diseases").addEventListener("click", handleCommand, false);
    document.getElementById("Respiratory_Infectious").addEventListener("click", handleCommand, false);



    // Set up the legend
    // const legend = L.control({ position: "bottomleft" });
    //
    // legend.onAdd = function() {
    //     const div = L.DomUtil.create("div", "info legend");
    //     const limits = geojson.options.limits;
    //     const colors = geojson.options.colors;
    //
    //     // Add min & max
    //     const legendInfo = "<h1>Cardiovascular Disease</h1>" +
    //     "<div class=\"labels\">" +
    //     "<div class=\"min\">" + limits[0] + "</div>" +
    //     "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
    //     "</div>";
    //
    //     div.innerHTML = legendInfo;
    //
    //     const labels = limits.map((limit, index) => {
    //         return "<li style=\"background-color: " + colors[index] + "\"></li>"
    //     })
    //
    //     div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    //     return div;
    // };

    // Adding legend to the map
    // ...
    // legend.addTo(myMap)

    // L.control.layers(baseMaps, overlayMaps, {
    //         collapsed: false
    // }).addTo(myMap);
})()
