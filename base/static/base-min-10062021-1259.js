const modal = () => { document.addEventListener("DOMContentLoaded", function (e) { $("#form-modal").on("show.bs.modal", function (e) { var o = $(e.relatedTarget), t = o.data("start"), a = o.data("off"), i = o.data("leftoff"), r = o.data("nobleman"), n = o.data("leftnobleman"), l = o.data("id"), d = $(this); d.find(".modal-title").text(t), d.find("#id_off").val(a), d.find("#id_off").attr("max", parseInt(a) + parseInt(i)), d.find("#id_nobleman").val(r), d.find("#id_nobleman").attr("max", parseInt(r) + parseInt(n)), d.find("#id_weight_id").val(l) }), $(".popoverData").popover(), $(".popoverOption").popover({ trigger: "hover" }) }) }, scroll_content_outline = () => { $(window).on("load", function () { null != localStorage.getItem("my_app_name_here-quote-scroll") && $(window).scrollTop(localStorage.getItem("my_app_name_here-quote-scroll")), null != localStorage.getItem("my_app_name_here-left-scroll") && $("#leftscroll").scrollTop(localStorage.getItem("my_app_name_here-left-scroll")), $(window).on("scroll", function () { localStorage.setItem("my_app_name_here-quote-scroll", $(window).scrollTop()) }), $("#leftscroll").on("scroll", function () { var e = $("#leftscroll").scrollTop(); localStorage.setItem("my_app_name_here-left-scroll", e) }) }) }, menu_toggle = () => { $("#menu-toggle").click(function (e) { e.preventDefault(), $("#sidebar-wrapper").toggleClass("toggled") }), $(document).ready(function () { $("#id_date").addClass("data-picker"), $(".data-picker").datepicker({ format: "yyyy-mm-dd" }) }) }, calculate_distance = e => { const o = parseFloat(String(document.getElementById("speed_world").value).replace(",", ".")), t = parseFloat(String(document.getElementById("speed_units").value).replace(",", ".")); if (e.clicked) e.innerHTML = e.distance, e.clicked = !1; else { e.distance = parseFloat(e.innerHTML); let a = e.distance / t / o / 60 * 30; a = a > 99.9 ? a.toFixed(0) : a.toFixed(1); let i = e.distance / t / o / 60 * 35; i = i > 99.9 ? i.toFixed(0) : i.toFixed(1), e.innerHTML = `<span class='text-nowrap'>${a}h / ${i}h</span>`, e.clicked = !0 } }, activateTooltips = () => { document.addEventListener("DOMContentLoaded", function (e) { $(".popoverData").popover() }), $(function () { $('[data-toggle="tooltip"]').tooltip() }) }, onPlanerLinkClick = e => { setTimeout(() => { document.getElementById("planer-link").innerHTML = `<span class='spinner-border mr-1 spinner-border-sm text-info my-auto' role='status'></span>${e}` }, 800) }, handleAllFormsetSelect = () => { document.addEventListener("DOMContentLoaded", function (e) { val = $("#id_form-0-status").val(), "all" === val ? ($("#id_form-0-from_number").val(""), $("#id_form-0-from_number").prop("disabled", !0), $("#id_form-0-to_number").val(""), $("#id_form-0-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-0-from_number").val(""), $("#id_form-0-from_number").prop("disabled", !0), $("#id_form-0-to_number").prop("disabled", !1)), val = $("#id_form-1-status").val(), "all" === val ? ($("#id_form-1-from_number").val(""), $("#id_form-1-from_number").prop("disabled", !0), $("#id_form-1-to_number").val(""), $("#id_form-1-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-1-from_number").val(""), $("#id_form-1-from_number").prop("disabled", !0), $("#id_form-1-to_number").prop("disabled", !1)), val = $("#id_form-2-status").val(), "all" === val ? ($("#id_form-2-from_number").val(""), $("#id_form-2-from_number").prop("disabled", !0), $("#id_form-2-to_number").val(""), $("#id_form-2-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-2-from_number").val(""), $("#id_form-2-from_number").prop("disabled", !0), $("#id_form-2-to_number").prop("disabled", !1)), val = $("#id_form-3-status").val(), "all" === val ? ($("#id_form-3-from_number").val(""), $("#id_form-3-from_number").prop("disabled", !0), $("#id_form-3-to_number").val(""), $("#id_form-3-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-3-from_number").val(""), $("#id_form-3-from_number").prop("disabled", !0), $("#id_form-3-to_number").prop("disabled", !1)), val = $("#id_form-4-status").val(), "all" === val ? ($("#id_form-4-from_number").val(""), $("#id_form-4-from_number").prop("disabled", !0), $("#id_form-4-to_number").val(""), $("#id_form-4-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-4-from_number").val(""), $("#id_form-4-from_number").prop("disabled", !0), $("#id_form-4-to_number").prop("disabled", !1)), val = $("#id_form-5-status").val(), "all" === val ? ($("#id_form-5-from_number").val(""), $("#id_form-5-from_number").prop("disabled", !0), $("#id_form-5-to_number").val(""), $("#id_form-5-to_number").prop("disabled", !0)) : "exact" === val && ($("#id_form-5-from_number").val(""), $("#id_form-5-from_number").prop("disabled", !0), $("#id_form-5-to_number").prop("disabled", !1)) }), document.addEventListener("DOMContentLoaded", function (e) { $(".time-timepicker").each(function () { $(this).timepicker({ minuteStep: 1, secondStep: 1, showSeconds: !0, showMeridian: !1, defaultTime: !1, icons: { up: "fa fa-angle-up", down: "fa fa-angle-down" } }) }), $("#id_form-0-status").change(function () { val = $("#id_form-0-status").val(), "all" === val ? ($("#id_form-0-from_number").val(""), $("#id_form-0-from_number").prop("disabled", !0), $("#id_form-0-to_number").val(""), $("#id_form-0-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-0-from_number").val(""), $("#id_form-0-from_number").prop("disabled", !0), $("#id_form-0-to_number").prop("disabled", !1)) : ($("#id_form-0-from_number").prop("disabled", !1), $("#id_form-0-to_number").prop("disabled", !1)) }), $("#id_form-1-status").change(function () { val = $("#id_form-1-status").val(), "all" === val ? ($("#id_form-1-from_number").val(""), $("#id_form-1-from_number").prop("disabled", !0), $("#id_form-1-to_number").val(""), $("#id_form-1-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-1-from_number").val(""), $("#id_form-1-from_number").prop("disabled", !0), $("#id_form-1-to_number").prop("disabled", !1)) : ($("#id_form-1-from_number").prop("disabled", !1), $("#id_form-1-to_number").prop("disabled", !1)) }), $("#id_form-2-status").change(function () { val = $("#id_form-2-status").val(), "all" === val ? ($("#id_form-2-from_number").val(""), $("#id_form-2-from_number").prop("disabled", !0), $("#id_form-2-to_number").val(""), $("#id_form-2-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-2-from_number").val(""), $("#id_form-2-from_number").prop("disabled", !0), $("#id_form-2-to_number").prop("disabled", !1)) : ($("#id_form-2-from_number").prop("disabled", !1), $("#id_form-2-to_number").prop("disabled", !1)) }), $("#id_form-3-status").change(function () { val = $("#id_form-3-status").val(), "all" === val ? ($("#id_form-3-from_number").val(""), $("#id_form-3-from_number").prop("disabled", !0), $("#id_form-3-to_number").val(""), $("#id_form-3-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-3-from_number").val(""), $("#id_form-3-from_number").prop("disabled", !0), $("#id_form-3-to_number").prop("disabled", !1)) : ($("#id_form-3-from_number").prop("disabled", !1), $("#id_form-3-to_number").prop("disabled", !1)) }), $("#id_form-4-status").change(function () { val = $("#id_form-4-status").val(), "all" === val ? ($("#id_form-4-from_number").val(""), $("#id_form-4-from_number").prop("disabled", !0), $("#id_form-4-to_number").val(""), $("#id_form-4-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-4-from_number").val(""), $("#id_form-4-from_number").prop("disabled", !0), $("#id_form-4-to_number").prop("disabled", !1)) : ($("#id_form-4-from_number").prop("disabled", !1), $("#id_form-4-to_number").prop("disabled", !1)) }), $("#id_form-5-status").change(function () { val = $("#id_form-5-status").val(), "all" === val ? ($("#id_form-5-from_number").val(""), $("#id_form-5-from_number").prop("disabled", !0), $("#id_form-5-to_number").val(""), $("#id_form-5-to_number").prop("disabled", !0)) : "exact" === val ? ($("#id_form-5-from_number").val(""), $("#id_form-5-from_number").prop("disabled", !0), $("#id_form-5-to_number").prop("disabled", !1)) : ($("#id_form-5-from_number").prop("disabled", !1), $("#id_form-5-to_number").prop("disabled", !1)) }) }) }, handleClickButton = (e, o, t, a = "") => { e.disabled = !0, e.innerHTML = `<span class='spinner-border mr-1 spinner-border-sm text-dark my-auto' role='status'></span> ${o} <span id=${a}></span>`, document.getElementById(t).submit() }; function getCookie(e) { var o = null; if (document.cookie && "" != document.cookie) for (var t = document.cookie.split(";"), a = 0; a < t.length; a++) { var i = jQuery.trim(t[a]); if (i.substring(0, e.length + 1) == e + "=") { o = decodeURIComponent(i.substring(e.length + 1)); break } } return o } const changeTargetTime = async (e, o) => { const t = parseInt(e), a = parseInt(o), i = String(e) + "-time-" + String(o), r = document.getElementById(i), n = r.innerHTML; r.innerHTML = '<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>'; const l = await fetch(`/api/target-time-update/${t}/${a}/`, { method: "PUT", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" } }); if (200 !== l.status) { r.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>'; const e = r.className; r.className = "btn btn-lg btn-danger my-1 py-0 px-1 mr-1", setTimeout(() => { r.className = e, r.innerHTML = n, r.blur() }, 2e3) } else { const e = await l.json(); if (r.className = "btn btn-lg btn-primary my-1 py-0 px-1 mr-1", r.innerHTML = n, r.blur(), "none" !== e.old && e.old !== e.new) { document.getElementById(e.old).className = "btn btn-lg btn-light my-1 py-0 px-1 mr-1" } } }, deleteTarget = async e => { const o = parseInt(e), t = "target-btn-" + String(e), a = "target-row-" + String(e), i = document.getElementById(t), r = document.getElementById(a), n = i.innerHTML; i.disabled = !0, i.innerHTML = '<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>', 204 !== (await fetch(`/api/target-delete/${o}/`, { method: "DELETE", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" } })).status ? (i.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>', setTimeout(() => { i.innerHTML = n, i.blur() }, 2e3)) : r.style.display = "none" }, submitGoBackButton = e => { const o = document.getElementById("form1-btn"), t = document.getElementById("dismiss-btn"); o.onclick = (() => { o.disabled = !0, t.disabled = !0, o.innerHTML = `<span class='spinner-border mr-1 spinner-border-sm text-dark my-auto' role='status'></span>${e}`, document.getElementById("form1-form").submit() }) }, changeIsHiddenState = async (e, o) => { const t = document.getElementById(o), a = t.innerHTML; t.disabled = !0, t.innerHTML = '<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>'; const i = await fetch(`/api/overview-hide-state-update/${e}/${o}/`, { method: "PUT", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" } }); if (200 !== i.status) t.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg>', setTimeout(() => { t.innerHTML = a, t.blur() }, 2e3); else { const e = await i.json(); t.innerHTML = e.name, t.className = e.class, t.disabled = !1, t.blur() } }, changeBuildingsArray = async (e, o) => { const t = document.getElementById("multi-select-spinner"); t.innerHTML = '<div class="spinner-border spinner-border-sm text-secondary" role="status"></div>'; const a = { buildings: o }; await fetch(`/api/change-buildings-array/${e}/`, { method: "PUT", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" }, body: JSON.stringify(a) }).then(e => { 200 === e.status ? (t.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="green" class="bi bi-check" viewBox="0 0 16 16"><path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/></svg>', setTimeout(() => { t.innerHTML = "" }, 400)) : (t.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg> <span class="md-error">(Error in connection!)</span>', setTimeout(() => { t.innerHTML = "" }, 2e3)) }).catch(() => { t.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-exclamation-square" viewBox="0 0 16 16"><path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/><path d="M7.002 11a1 1 0 1 1 2 0 1 1 0 0 1-2 0zM7.1 4.995a.905.905 0 1 1 1.8 0l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 4.995z"/></svg> <span class="md-error">(Error in connection!)</span>', setTimeout(() => { t.innerHTML = "" }, 2e3) }) }, resetUserMessages = async () => { const e = document.getElementById("reset-svg"), o = document.getElementById("reset-span"); await fetch("/api/reset-user-messages/", { method: "PUT", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" } }).then(t => { 200 === t.status && (e.style.fill = "rgba(0,0,0,.5)", o.style.color = "rgba(0,0,0,.5)", o.innerHTML = "0") }) }, codemirrorValidation = (e, o) => { document.addEventListener("DOMContentLoaded", function (t) { $(o).addClass("CodeMirror-Invalid"); const a = $(o)[0].CodeMirror, i = JSON.parse(e); Object.entries(i).forEach(([e, o], t) => { 0 === t && a.scrollIntoView(parseInt(o.message)), a.addLineClass(parseInt(o.message), "wrap", "line-error") }) }) }, handleButtonClipboardUpdate = (e, o, t, a) => { const i = document.getElementById(o).textContent; navigator.clipboard.writeText(i), e.innerHTML = `<svg class='mr-2' width='1.4em' height='1.4em' viewBox='0 0 16 16' class='bi bi-check2-all' fill='green' ><path fill-rule='evenodd' d='M12.354 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z'/><path d='M6.25 8.043l-.896-.897a.5.5 0 1 0-.708.708l.897.896.707-.707zm1 2.414l.896.897a.5.5 0 0 0 .708 0l7-7a.5.5 0 0 0-.708-.708L8.5 10.293l-.543-.543-.707.707z'/></svg>${t}`, setTimeout(() => { e.innerHTML = `<svg class='mr-2'  width='1.3em' height='1.3em' viewBox='0 0 16 16' class='bi bi-arrow-counterclockwise' fill='currentColor'><path fill-rule='evenodd' d='M8 3a5 5 0 1 1-4.546 2.914.5.5 0 0 0-.908-.417A6 6 0 1 0 8 2v1z'/><path d='M8 4.466V.534a.25.25 0 0 0-.41-.192L5.23 2.308a.25.25 0 0 0 0 .384l2.36 1.966A.25.25 0 0 0 8 4.466z'/></svg>${a}`, e.blur() }, 1800) }, copyDataToClipboard = (e, o, t) => { const a = t ? document.getElementById(o).value : document.getElementById(o).textContent; navigator.clipboard.writeText(a), e.blur(); const i = e.innerHTML; e.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="green" class="bi bi-check2-all" viewBox="0 0 16 16"><path d="M12.354 4.354a.5.5 0 0 0-.708-.708L5 10.293 1.854 7.146a.5.5 0 1 0-.708.708l3.5 3.5a.5.5 0 0 0 .708 0l7-7zm-4.208 7l-.896-.897.707-.707.543.543 6.646-6.647a.5.5 0 0 1 .708.708l-7 7a.5.5 0 0 1-.708 0z"/><path d="M5.354 7.146l.896.897-.707.707-.897-.896a.5.5 0 1 1 .708-.708z"/></svg>', setTimeout(() => { e.innerHTML = i }, 600) }, removeOutline = (e, o, t, a) => { const i = document.getElementById(o), r = document.getElementById(t); e.disabled = !0, e.innerHTML = `<span class='spinner-border mr-1 spinner-border-sm text-dark my-auto' role='status'></span> ${a}`, i.disabled = !0, r.submit() }, imagePopupActivate = () => { window.onload = function () { var e = document.createElement("div"); e.id = "img_box", document.getElementsByTagName("body")[0].appendChild(e), idpopup_img_box = document.getElementById("img_box"), idpopup_img_box.style.top = 0, idpopup_img_box.style.left = 0, idpopup_img_box.style.opacity = 0, idpopup_img_box.style.width = "100%", idpopup_img_box.style.height = "100%", idpopup_img_box.style.display = "none", idpopup_img_box.style.position = "fixed", idpopup_img_box.style.cursor = "pointer", idpopup_img_box.style.textAlign = "center", idpopup_img_box.style.zIndex = z_index_dv_img_box, idpopup_img_box.style.backgroundColor = bg_color_img_box } }, img_box = e => { var o = "string" == typeof e ? e : e.src; vopa_img_box = 0; var t, a, i, r = window.innerHeight, n = window.innerWidth, l = new Image; l.src = o, l.onload = function () { t = l.height, wimg_img_box = l.width, idpopup_img_box.innerHTML = "<img src=" + o + ">", wimg_img_box > n ? idpopup_img_box.getElementsByTagName("img")[0].style.width = "90%" : t > r && (idpopup_img_box.getElementsByTagName("img")[0].style.height = "90%", t = 90 * r / 100), t < r ? (a = r / 2 - t / 2, idpopup_img_box.style.paddingTop = a + "px") : idpopup_img_box.style.paddingTop = "0px", "yes" == allow_hide_scroll_img_box && (document.body.style.overflow = "hidden"), idpopup_img_box.style.display = "block" }, "yes" == use_fade_inout_img_box ? i = setInterval(function () { vopa_img_box <= 1.1 ? (idpopup_img_box.style.opacity = vopa_img_box, vopa_img_box += speed_img_box) : (idpopup_img_box.style.opacity = 1, clearInterval(i)) }, 10) : idpopup_img_box.style.opacity = 1, window.onkeyup = function (e) { if (27 == e.keyCode) if ("yes" == use_fade_inout_img_box) var o = setInterval(function () { vopa_img_box >= 0 ? (idpopup_img_box.style.opacity = vopa_img_box, vopa_img_box -= speed_img_box) : (idpopup_img_box.style.opacity = 0, clearInterval(o), idpopup_img_box.style.display = "none", idpopup_img_box.innerHTML = "", document.body.style.overflow = "visible", vopa_img_box = 0) }, 10); else idpopup_img_box.style.opacity = 0, idpopup_img_box.style.display = "none", idpopup_img_box.innerHTML = "", document.body.style.overflow = "visible" }, idpopup_img_box.onclick = function () { if ("yes" == use_fade_inout_img_box) var e = setInterval(function () { vopa_img_box >= 0 ? (idpopup_img_box.style.opacity = vopa_img_box, vopa_img_box -= speed_img_box) : (idpopup_img_box.style.opacity = 0, clearInterval(e), idpopup_img_box.style.display = "none", idpopup_img_box.innerHTML = "", document.body.style.overflow = "visible", vopa_img_box = 0) }, 10); else idpopup_img_box.style.opacity = 0, idpopup_img_box.style.display = "none", idpopup_img_box.innerHTML = "", document.body.style.overflow = "visible" } }, updateClipboard = e => { const o = document.getElementById(e).textContent; navigator.clipboard.writeText(o) }, updateAfterClick = async (e, o, t) => { const a = Number.parseFloat(o) / 100; let i = 0; const r = setInterval(() => { i += 1, e.innerHTML = t + ` ${i}%`, 99 === i && clearInterval(r) }, a) }, createBuildingsOptions = (e, o, t, a, i, r, n, l, d, s, m, p, _, b, u) => [{ label: e, value: "headquarters" }, { label: o, value: "barracks" }, { label: t, value: "stable" }, { label: a, value: "workshop" }, { label: i, value: "academy" }, { label: r, value: "smithy" }, { label: n, value: "rally_point" }, { label: l, value: "statue" }, { label: d, value: "market" }, { label: s, value: "timber_camp" }, { label: m, value: "clay_pit" }, { label: p, value: "iron_mine" }, { label: _, value: "farm" }, { label: b, value: "warehouse" }, { label: u, value: "wall" }], changeTextToSent = (e, o) => { e.innerHTML = `${o}` }, fillAndSubmit = e => { const o = document.getElementById("create-form"); document.getElementsByName("target_type")[0].value = e, o.submit() }, initialize_payment_process = e => { const o = document.getElementById("payment-button"); o.disabled = !0, fetch("/api/stripe-key/", { method: "GET", credentials: "same-origin", headers: { "X-CSRFToken": getCookie("csrftoken"), Accept: "application/json", "Content-Type": "application/json" } }).then(e => e.json()).then(t => { const a = Stripe(t.publicKey); o.onclick = (() => { fetch(`/api/stripe-session/${e}`).then(e => e.json()).then(e => a.redirectToCheckout({ sessionId: e.sessionId })) }), o.disabled = !1 }) };