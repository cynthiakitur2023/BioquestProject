$(document).ready(function() {
  var slider = $('.slider');
  var slideWidth = slider.find('.slide').outerWidth();
  var slideCount = slider.find('.slide').length;
  var visibleSlides = Math.floor($('.slider-container').width() / slideWidth);
  var currentIndex = 0;

  // Update the slider width based on slide count
  slider.css('width', slideWidth * slideCount);

  // Next button click event
  $('#nextBtn').click(function() {
    if (currentIndex < slideCount - visibleSlides) {
      currentIndex++;
      slide();
    }
  });

  // Previous button click event
  $('#prevBtn').click(function() {
    if (currentIndex > 0) {
      currentIndex--;
      slide();
    }
  });

  function slide() {
    var slidePosition = -1 * currentIndex * slideWidth;
    slider.css('transform', 'translateX(' + slidePosition + 'px)');
  }
});
