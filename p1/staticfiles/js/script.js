(function($) {
	
	"use strict";
/*
  *//* Mobile Menu */


  // init Chocolat light box
  var initChocolat = function() {
  Chocolat(document.querySelectorAll('.image-link'), {
      imageSize: 'contain',
      loop: true,
    })
  }

  $(document).ready(function () {
    MobileMenu();
    initChocolat();

    /*slider*/
    var swiper = new Swiper(".mySwiper", {
      autoHeight: true,
      spaceBetween: 20,
      navigation: {
        nextEl: ".slide-button-next",
        prevEl: ".slide-button-prev",
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

    /* Video */
    var $videoSrc;  
    $('.play-btn').click(function() {
        $videoSrc = $(this).data( "src" );
    });

    $('#myModal').on('shown.bs.modal', function (e) {

    $("#video").attr('src',$videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0" ); 
    })

    $('#myModal').on('hide.bs.modal', function (e) {
      $("#video").attr('src',$videoSrc); 
    })

    function initializeChart() {
      /*circle progress bar*/
      $('.chart').easyPieChart({
        easing: 'easeOutBounce',
        size: '290',
        lineWidth: '1',
        barColor: '#E8E8E8',
        trackColor: '#fff',
        scaleColor: '#fff',
        lineCap: 'square',
        animate: {
          duration: 4000,
          enabled: true
        },
        onStep: function(from, to, percent) {
          $(this.el).find('.percent').text(Math.round(percent));
        }
      });
      var chart = window.chart = $('.chart').data('easyPieChart');
      $('.js_update').on('click', function() {
        chart.update(Math.random()*200-100);
      });
    }

    function handleIntersection(entries, observer) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {          
          initializeChart();
          observer.unobserve(entry.target);
        }
      });
    }

    const observer = new IntersectionObserver(handleIntersection);

    const servicesWrap = document.getElementsByClassName('services-wrap')[0];
    observer.observe(servicesWrap);

  });

  // window.addEventListener("load", function () {
  //   /* Preloader */
  //   const preloader = document.getElementById("preloader");
  //   preloader.classList.add("hide-preloader");
  // });

})(window.jQuery);