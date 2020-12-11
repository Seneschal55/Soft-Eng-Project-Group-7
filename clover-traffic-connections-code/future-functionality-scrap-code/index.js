// Initialize and add the map
function initMap() {
    // The location of Uluru
    const bloom = { lat: 39.15, lng: -86.5 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: bloom,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: bloom,
      map: map,
    });
  }