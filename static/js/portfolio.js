/**
 * Created by codyhelbling on 9/30/16.
 */

$('.wrap').mouseover(function () {
    $('.company-image-overlay').show();
}).mouseout(function () {
    $('.company-image-overlay').hide();
});

$('.image').mouseover(function(){
   $('.proj_pic_text').css('opacity', 1)
});


$('.image').mouseout(function(){
   $('.proj_pic_text').css('opacity', 0)
});
