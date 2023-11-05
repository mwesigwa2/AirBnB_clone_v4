$(document).ready(function() {
  const amenityIds = {};

  $('input[type="checkbox"]').on('change', function() {
    const amenityId = $(this).data('id'); // Get Amenity ID from data-id attribute

    if ($(this).is(':checked')) {
      amenityIds[amenityId] = true;
    } else {
      delete amenityIds[amenityId];
    }

    const amenitiesList = [];
    for (const id in amenityIds) {
      const amenityName = $('input[data-id="' + id + '"]').data('name');
      amenitiesList.push(amenityName);
    }

    $('.amenities h4').text(amenitiesList.join(', '));
  });
});
$.get('http://0.0.0.0:5001/api/v1/status/', function (data, textStatus) {
    if (data.status === 'OK') {
      $('#api-status').addClass('available');
    }
  })
});
