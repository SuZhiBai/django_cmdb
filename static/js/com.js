/**
 * Created by ybzhang on 2016/9/24.
 */
function showHint(str)
{
var xmlhttp;
if (str.length==0)
  {
  document.getElementById("txtHint").innerHTML="";
  return;
  }
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","/search?host="+str,true);
xmlhttp.send();
}

jQuery(document).ready(function($) {
	$('.theme-hostname-init').click(function(){
		$('.theme-popover-mask').fadeIn(100);
		$('.theme-popover').slideDown(200);
	})
	$('.theme-poptit .close').click(function(){
		$('.theme-popover-mask').fadeOut(100);
		$('.theme-popover').slideUp(200);
	})

})

$(document).ready(function($) {
        $('.theme-host-modify').click(function(){
                $('.theme-popover-host').slideDown(200);
        })
        $('.theme-poptit-host .close').click(function(){
                $('.theme-popover-host').slideUp(200);
        })

})

$(document).ready(function($) {
        $('.theme-isp-modify').click(function(){
                $('.theme-popover-isp-mask').fadeIn(100);
                $('.theme-popover-isp').slideDown(200);
        })
        $('.theme-poptit-isp .close').click(function(){
                $('.theme-popover-isp-mask').fadeOut(100);
                $('.theme-popover-isp').slideUp(200);
        })

})

// $(document).ready(function($) {
//         $('.theme-idc-modify').click(function(){
//                 $('.theme-popover-idc').slideDown(200);
//         })
//
// })

jQuery(document).ready(function($) {
        $('.theme-maintance-modify').click(function(){
                $('.theme-popover-maintance-mask').fadeIn(100);
                $('.theme-popover-maintance').slideDown(200);
        })
        $('.theme-poptit-maintance .close').click(function(){
                $('.theme-popover-maintance-mask').fadeOut(100);
                $('.theme-popover-maintance').slideUp(200);
        })

})

jQuery(document).ready(function($) {
        $('.theme-idc-delete').click(function(){
                $('.theme-popover-idc-delete-mask').fadeIn(100);
                $('.theme-popover-idc-delete').slideDown(200);
        })
        $('.theme-poptit-idc-delete .close').click(function(){
                $('.theme-popover-idc-delete-mask').fadeOut(100);
                $('.theme-popover-idc-delete').slideUp(200);
        })

})


