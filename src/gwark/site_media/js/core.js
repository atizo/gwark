jQuery.extend(jQuery.easing, {
	easeInOutCubic: function (x, t, b, c, d) {
		if((t/=d/2) < 1){
			return c/2*t*t*t + b;
		}
		return c/2*((t-=2)*t*t + 2) + b;
	}
});

var gw = {};
gw.anim = {};
gw.anim.step = 0;

gw.adjustSlider = function(){
	var viewportWidth = $(window).width();
	$('ul#slideshow_list').width(viewportWidth * 4);
	$('ul#slideshow_list li').width(viewportWidth);
	var h = viewportWidth * 0.4;
	if(h > 500){ h = 500; }	
	$('ul#slideshow_list').height(h);	
};

gw.endless = function(){
	
	if(gw.anim.step == 3){
		$('ul#slideshow_list').css('left', 0);
		gw.anim.step = 0
	}
	
	gw.anim.step += 1;	
	
	$('ul#slideshow_list').animate({
		left: gw.anim.step * -$(window).width()
		
	}, 1200, "easeInOutCubic", function() {
		setTimeout(gw.endless, 2000);
	});	
};


gw.init = function(){
	
	gw.adjustSlider();
	$('#slideshow_container').show();
	
	$(window).resize(function() {
		gw.adjustSlider();
	});
	
	gw.endless();
};