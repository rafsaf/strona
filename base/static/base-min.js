const modal=()=>{document.addEventListener("DOMContentLoaded",function(e){$("#form-modal").on("show.bs.modal",function(e){var o=$(e.relatedTarget),r=o.data("start"),t=o.data("off"),a=o.data("leftoff"),n=o.data("nobleman"),d=o.data("leftnobleman"),i=o.data("id"),l=$(this);l.find(".modal-title").text(r),l.find("#id_off").val(t),l.find("#id_off").attr("max",parseInt(t)+parseInt(a)),l.find("#id_nobleman").val(n),l.find("#id_nobleman").attr("max",parseInt(n)+parseInt(d)),l.find("#id_weight_id").val(i)}),$(".popoverData").popover(),$(".popoverOption").popover({trigger:"hover"})})},scroll_content_outline=()=>{$(window).on("load",function(){null!=localStorage.getItem("my_app_name_here-quote-scroll")&&$(window).scrollTop(localStorage.getItem("my_app_name_here-quote-scroll")),null!=localStorage.getItem("my_app_name_here-left-scroll")&&$("#leftscroll").scrollTop(localStorage.getItem("my_app_name_here-left-scroll")),$(window).on("scroll",function(){localStorage.setItem("my_app_name_here-quote-scroll",$(window).scrollTop())}),$("#leftscroll").on("scroll",function(){var e=$("#leftscroll").scrollTop();localStorage.setItem("my_app_name_here-left-scroll",e)})})},menu_toggle=()=>{$("#menu-toggle").click(function(e){e.preventDefault(),$("#sidebar-wrapper").toggleClass("toggled")}),$(document).ready(function(){$("#id_date").addClass("data-picker"),$(".data-picker").datepicker({format:"yyyy-mm-dd"})})},calculate_distance=e=>{const o=parseFloat(String(document.getElementById("speed_world").value).replace(",",".")),r=parseFloat(String(document.getElementById("speed_units").value).replace(",","."));if(e.clicked)e.innerHTML=e.distance,e.clicked=!1;else{e.distance=parseFloat(e.innerHTML);let t=e.distance/r/o/60*30;t=t>99.9?t.toFixed(0):t.toFixed(1);let a=e.distance/r/o/60*35;a=a>99.9?a.toFixed(0):a.toFixed(1),e.innerHTML=`<span class='text-nowrap'>${t}h / ${a}h</span>`,e.clicked=!0}};function labnolIframe(e){var o=document.createElement("iframe");o.setAttribute("src","https://www.youtube.com/embed/"+e.dataset.id+"?autoplay=1&rel=0"),o.setAttribute("frameborder","0"),o.setAttribute("allowfullscreen","1"),o.setAttribute("allow","accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"),e.parentNode.replaceChild(o,e)}function initYouTubeVideos(){for(var e=document.getElementsByClassName("youtube-player"),o=0;o<e.length;o++){var r=e[o].dataset.id,t=document.createElement("div");t.setAttribute("data-id",r);var a=document.createElement("img");a.src="//i.ytimg.com/vi/ID/hqdefault.jpg".replace("ID",r),t.appendChild(a);var n=document.createElement("div");n.setAttribute("class","play"),t.appendChild(n),t.onclick=function(){labnolIframe(this)},e[o].appendChild(t)}}const activateTooltips=()=>{document.addEventListener("DOMContentLoaded",function(e){$(".popoverData").popover()}),$(function(){$('[data-toggle="tooltip"]').tooltip()})},onPlanerLinkClick=e=>{setTimeout(()=>{document.getElementById("planer-link").innerHTML=`<span class='spinner-border mr-1 spinner-border-sm text-info my-auto' role='status'></span>${e}`},800)},handleAllFormsetSelect=()=>{document.addEventListener("DOMContentLoaded",function(e){val=$("#id_form-0-status").val(),"all"===val?($("#id_form-0-from_number").val(""),$("#id_form-0-from_number").prop("disabled",!0),$("#id_form-0-to_number").val(""),$("#id_form-0-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-0-from_number").val(""),$("#id_form-0-from_number").prop("disabled",!0),$("#id_form-0-to_number").prop("disabled",!1)),val=$("#id_form-1-status").val(),"all"===val?($("#id_form-1-from_number").val(""),$("#id_form-1-from_number").prop("disabled",!0),$("#id_form-1-to_number").val(""),$("#id_form-1-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-1-from_number").val(""),$("#id_form-1-from_number").prop("disabled",!0),$("#id_form-1-to_number").prop("disabled",!1)),val=$("#id_form-2-status").val(),"all"===val?($("#id_form-2-from_number").val(""),$("#id_form-2-from_number").prop("disabled",!0),$("#id_form-2-to_number").val(""),$("#id_form-2-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-2-from_number").val(""),$("#id_form-2-from_number").prop("disabled",!0),$("#id_form-2-to_number").prop("disabled",!1)),val=$("#id_form-3-status").val(),"all"===val?($("#id_form-3-from_number").val(""),$("#id_form-3-from_number").prop("disabled",!0),$("#id_form-3-to_number").val(""),$("#id_form-3-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-3-from_number").val(""),$("#id_form-3-from_number").prop("disabled",!0),$("#id_form-3-to_number").prop("disabled",!1)),val=$("#id_form-4-status").val(),"all"===val?($("#id_form-4-from_number").val(""),$("#id_form-4-from_number").prop("disabled",!0),$("#id_form-4-to_number").val(""),$("#id_form-4-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-4-from_number").val(""),$("#id_form-4-from_number").prop("disabled",!0),$("#id_form-4-to_number").prop("disabled",!1)),val=$("#id_form-5-status").val(),"all"===val?($("#id_form-5-from_number").val(""),$("#id_form-5-from_number").prop("disabled",!0),$("#id_form-5-to_number").val(""),$("#id_form-5-to_number").prop("disabled",!0)):"exact"===val&&($("#id_form-5-from_number").val(""),$("#id_form-5-from_number").prop("disabled",!0),$("#id_form-5-to_number").prop("disabled",!1))}),document.addEventListener("DOMContentLoaded",function(e){$(".time-timepicker").each(function(){$(this).timepicker({minuteStep:1,secondStep:1,showSeconds:!0,showMeridian:!1,defaultTime:!1,icons:{up:"fa fa-angle-up",down:"fa fa-angle-down"}})}),$("#id_form-0-status").change(function(){val=$("#id_form-0-status").val(),"all"===val?($("#id_form-0-from_number").val(""),$("#id_form-0-from_number").prop("disabled",!0),$("#id_form-0-to_number").val(""),$("#id_form-0-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-0-from_number").val(""),$("#id_form-0-from_number").prop("disabled",!0),$("#id_form-0-to_number").prop("disabled",!1)):($("#id_form-0-from_number").prop("disabled",!1),$("#id_form-0-to_number").prop("disabled",!1))}),$("#id_form-1-status").change(function(){val=$("#id_form-1-status").val(),"all"===val?($("#id_form-1-from_number").val(""),$("#id_form-1-from_number").prop("disabled",!0),$("#id_form-1-to_number").val(""),$("#id_form-1-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-1-from_number").val(""),$("#id_form-1-from_number").prop("disabled",!0),$("#id_form-1-to_number").prop("disabled",!1)):($("#id_form-1-from_number").prop("disabled",!1),$("#id_form-1-to_number").prop("disabled",!1))}),$("#id_form-2-status").change(function(){val=$("#id_form-2-status").val(),"all"===val?($("#id_form-2-from_number").val(""),$("#id_form-2-from_number").prop("disabled",!0),$("#id_form-2-to_number").val(""),$("#id_form-2-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-2-from_number").val(""),$("#id_form-2-from_number").prop("disabled",!0),$("#id_form-2-to_number").prop("disabled",!1)):($("#id_form-2-from_number").prop("disabled",!1),$("#id_form-2-to_number").prop("disabled",!1))}),$("#id_form-3-status").change(function(){val=$("#id_form-3-status").val(),"all"===val?($("#id_form-3-from_number").val(""),$("#id_form-3-from_number").prop("disabled",!0),$("#id_form-3-to_number").val(""),$("#id_form-3-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-3-from_number").val(""),$("#id_form-3-from_number").prop("disabled",!0),$("#id_form-3-to_number").prop("disabled",!1)):($("#id_form-3-from_number").prop("disabled",!1),$("#id_form-3-to_number").prop("disabled",!1))}),$("#id_form-4-status").change(function(){val=$("#id_form-4-status").val(),"all"===val?($("#id_form-4-from_number").val(""),$("#id_form-4-from_number").prop("disabled",!0),$("#id_form-4-to_number").val(""),$("#id_form-4-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-4-from_number").val(""),$("#id_form-4-from_number").prop("disabled",!0),$("#id_form-4-to_number").prop("disabled",!1)):($("#id_form-4-from_number").prop("disabled",!1),$("#id_form-4-to_number").prop("disabled",!1))}),$("#id_form-5-status").change(function(){val=$("#id_form-5-status").val(),"all"===val?($("#id_form-5-from_number").val(""),$("#id_form-5-from_number").prop("disabled",!0),$("#id_form-5-to_number").val(""),$("#id_form-5-to_number").prop("disabled",!0)):"exact"===val?($("#id_form-5-from_number").val(""),$("#id_form-5-from_number").prop("disabled",!0),$("#id_form-5-to_number").prop("disabled",!1)):($("#id_form-5-from_number").prop("disabled",!1),$("#id_form-5-to_number").prop("disabled",!1))})})},handleClickButton=(e,o,r)=>{e.disabled=!0,e.innerHTML=`<span class='spinner-border mr-1 spinner-border-sm text-dark my-auto' role='status'></span>${o}`,document.getElementById(r).submit()};function getCookie(e){var o=null;if(document.cookie&&""!=document.cookie)for(var r=document.cookie.split(";"),t=0;t<r.length;t++){var a=jQuery.trim(r[t]);if(a.substring(0,e.length+1)==e+"="){o=decodeURIComponent(a.substring(e.length+1));break}}return o}const changeTargetTime=async(e,o)=>{const r=parseInt(e),t=parseInt(o),a=String(e)+"-time-"+String(o),n=document.getElementById(a),d=n.innerHTML;n.innerHTML='<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>';const i=await fetch(`/api/target-time-update/${r}/${t}/`,{method:"PUT",credentials:"same-origin",headers:{"X-CSRFToken":getCookie("csrftoken"),Accept:"application/json","Content-Type":"application/json"}});if(200!==i.status){n.innerHTML='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>';const e=n.className;n.className="btn btn-lg btn-danger my-1 py-0 px-1",setTimeout(()=>{n.className=e,n.innerHTML=d,n.blur()},2e3)}else{const e=await i.json();if(n.className="btn btn-lg btn-primary my-1 py-0 px-1",n.innerHTML=d,n.blur(),"none"!==e.old&&e.old!==e.new){document.getElementById(e.old).className="btn btn-lg btn-light my-1 py-0 px-1"}}},deleteTarget=async e=>{const o=parseInt(e),r="target-btn-"+String(e),t="target-row-"+String(e),a=document.getElementById(r),n=document.getElementById(t),d=a.innerHTML;a.disabled=!0,a.innerHTML='<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>',204!==(await fetch(`/api/target-delete/${o}/`,{method:"DELETE",credentials:"same-origin",headers:{"X-CSRFToken":getCookie("csrftoken"),Accept:"application/json","Content-Type":"application/json"}})).status?(a.innerHTML='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>',setTimeout(()=>{a.innerHTML=d,a.blur()},2e3)):n.style.display="none"},submitGoBackButton=e=>{const o=document.getElementById("form1-btn"),r=document.getElementById("dismiss-btn");o.onclick=(()=>{o.disabled=!0,r.disabled=!0,o.innerHTML=`<span class='spinner-border mr-1 spinner-border-sm text-dark my-auto' role='status'></span>${e}`,document.getElementById("form1-form").submit()})},activateFixedScrollbarContainer=()=>{document.addEventListener("DOMContentLoaded",function(e){$(function(e){var o={display:"none",overflowX:"scroll",position:"fixed",width:"100%",bottom:0};e(".fixed-scrollbar-container").each(function(){var r=e(this),t=e('<div class="fixed-scrollbar"><div></div></div>').appendTo(r).css(o);t.scroll(function(){r.scrollLeft(t.scrollLeft())}),t.data("status","off")});e(window).on("load.fixedbar resize.fixedbar",function(){e(".fixed-scrollbar").each(function(){var o=e(this),r=o.parent();o.children("div").height(1).width(r[0].scrollWidth),o.width(r.width()).scrollLeft(r.scrollLeft())})});var r=null;e(window).on("scroll.fixedbar",function(){clearTimeout(r),r=setTimeout(function(){e(".fixed-scrollbar-container").each(function(){var o=e(this),r=o.children(".fixed-scrollbar");if(r.length){var t={top:o.offset().top,bottom:o.offset().top+o.height()},a={top:e(window).scrollTop(),bottom:e(window).scrollTop()+e(window).height()};t.top>a.bottom||a.bottom>t.bottom?"on"==r.data("status")&&r.hide().data("status","off"):"off"==r.data("status")&&(r.show().data("status","on"),r.scrollLeft(o.scrollLeft()))}})},50)}),e(window).trigger("scroll.fixedbar")})})},changeIsHiddenState=async(e,o)=>{const r=document.getElementById(o),t=r.innerHTML;r.disabled=!0,r.innerHTML='<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>';const a=await fetch(`/api/overview-hide-state-update/${e}/${o}/`,{method:"PUT",credentials:"same-origin",headers:{"X-CSRFToken":getCookie("csrftoken"),Accept:"application/json","Content-Type":"application/json"}});if(200!==a.status)r.innerHTML='<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>',setTimeout(()=>{r.innerHTML=t,r.blur()},2e3);else{const e=await a.json();r.innerHTML=e.name,r.className=e.class,r.disabled=!1,r.blur()}},codemirrorValidation=(e,o)=>{document.addEventListener("DOMContentLoaded",function(r){$(o).addClass("CodeMirror-Invalid");const t=$(o)[0].CodeMirror,a=JSON.parse(e);Object.entries(a).forEach(([e,o],r)=>{0===r&&t.scrollIntoView(parseInt(o.message)),t.addLineClass(parseInt(o.message),"wrap","line-error")})})};