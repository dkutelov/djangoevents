 function initMap() {
        const mapContainer = document.getElementById("event-map");
        const lat = Number(mapContainer.dataset.lat);
        const lng = Number(mapContainer.dataset.lng);

        const eventPosition = { lat, lng };
        const map = new google.maps.Map(mapContainer, {
          zoom: 15,
          center: eventPosition,
        });
        const marker = new google.maps.Marker({
          position: eventPosition,
          map: map,
        });
      }