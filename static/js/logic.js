// Creating map object
var myMap = L.map("map", {
    center: [40.7128, -74.0059],
    zoom: 2
});

// Adding tile layer
// console.log(`api key: ${API_KEY}`)
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
}).addTo(myMap);

// console.log(myMap)
//
(async function(){
    // Link to GeoJSON
    const APILink = "/daly";
    // Grab data with D3
    // ...
    data = await d3.json(APILink)
    // console.log(data)
    // Create a new choropleth layer
    var geojson = L.choropleth(data, {

        // Define what  property in the features to use
        // ...
        valueProperty: 'Cardiovascular_diseases',
        scale: ['yellow', 'red'],
        steps: 20,
        mode: 'q',
        style: {
            // Border color
            // ...
            color: '#fff',
            weight: 1,
            fillOpacity: 0.8
        },

        // Binding a pop-up to each layer
        onEachFeature: function(feature, layer) {
            // const popupMsg = feature.properties.LOCALNAME + ", " + feature.properties.State + "<br>Median Household Income:<br>" + "$" + feature.properties.MHI
            const popupMsg = feature.properties.name
            // ...
        }
    }).addTo(myMap);

    var geojson = L.choropleth(data, {

        // Define what  property in the features to use
        // ...
        valueProperty: 'Respiratory_Infectious',
        scale: ['blue', 'purple'],
        steps: 20,
        mode: 'q',
        style: {
            // Border color
            // ...
            color: '#fff',
            weight: 1,
            fillOpacity: 0.8
        },

        // Binding a pop-up to each layer
        onEachFeature: function(feature, layer) {
            // const popupMsg = feature.properties.LOCALNAME + ", " + feature.properties.State + "<br>Median Household Income:<br>" + "$" + feature.properties.MHI
            const popupMsg = feature.properties.name
            // ...
        }
    }).addTo(myMap);

    // Set up the legend
    const legend = L.control({ position: "bottomleft" });
    legend.onAdd = function() {
        const div = L.DomUtil.create("div", "info legend");
        const limits = geojson.options.limits;
        const colors = geojson.options.colors;

        // Add min & max
        const legendInfo = "<h1>Cardiovascular Disease</h1>" +
        "<div class=\"labels\">" +
        "<div class=\"min\">" + limits[0] + "</div>" +
        "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
        "</div>";

        div.innerHTML = legendInfo;

        const labels = limits.map((limit, index) => {
            return "<li style=\"background-color: " + colors[index] + "\"></li>"
        })

        div.innerHTML += "<ul>" + labels.join("") + "</ul>";
        return div;
    };

    // Adding legend to the map
    // ...
    legend.addTo(myMap)
})()
