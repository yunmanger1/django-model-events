function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}
if (!socket_uri){
    var socket_uri = window.location.pathname + "ws";
}
var socket = new WebSocket(window.location.origin.replace('http', 'ws') + socket_uri + "?session_key=" + getCookie("sessionid"));

socket.onopen = function () {
    var event = new CustomEvent("websocket.open");
    window.dispatchEvent(event);

};
socket.onmessage = function(e) {
    if (e.data === "PONG") return;
    var $data = JSON.parse(e.data);
    var event = new CustomEvent("websocket." + $data.type, {detail: $data});
    window.dispatchEvent(event);
};
socket.onclose = function() {
    var event = new CustomEvent("websocket.close");
    window.dispatchEvent(event);
};
