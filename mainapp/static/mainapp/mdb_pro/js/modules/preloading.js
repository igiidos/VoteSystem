"use strict";

// 'use strict';
var windowLoaded = false;
$(window).on('load', function () {
  windowLoaded = true;
});
$(document).ready(function () {
  $('body').attr('aria-busy', true);
  $('#preloader-markup').load('../dev/dist/mdb-addons/preloader.html', function () {
    if (windowLoaded) {
      $('#mdb-preloader').fadeOut('slow');
      $('body').removeAttr('aria-busy');
    } else {
      $(window).on('load', function () {
        $('#mdb-preloader').fadeOut('slow');
        $('body').removeAttr('aria-busy');
      });
    }
  });
});