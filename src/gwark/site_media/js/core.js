jQuery.extend( jQuery.easing,
	{
		easeInOutCubic: function (x, t, b, c, d) {
		if ((t/=d/2) < 1) return c/2*t*t*t + b;
		return c/2*((t-=2)*t*t + 2) + b;
	}
});

var gw = {};
gw.anim = {};
gw.anim.step = 0;

gw.adjustSlider = function(){
	var viewportWidth = $(window).width();
	$('div#slideshow_container').height(viewportWidth * 0.4);
	$('ul#slideshow_list').width(viewportWidth * 4);
	$('ul#slideshow_list li').width(viewportWidth);
	//todo clear timeout
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

gw.facebookConnect = function(form){
    function handleResponse(response){
        form.submit();
    }
    FB.login(handleResponse, {perms: 'email' }  );
}


gw.init = function(){
	//load slider images asyc
	$('img.slideimg2').attr('src', 'http://assets.tumblr.com/images/register_login/dashboard.png');
	$('img.slideimg3').attr('src', 'http://assets.tumblr.com/images/register_login/phones.png').load(function(){
		gw.adjustSlider();
		$('#slideshow_container').show();						
		gw.endless();
    });
	
	$(window).resize(function() {
		gw.adjustSlider();
	});
	
	$("a#example1").fancybox({padding: 0, speedIn: 200, speedOut: 100});
};