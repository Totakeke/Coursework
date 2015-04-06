// We don't yet have an API to know when an element is updated, so we'll poll
// and if we find the content has changed, we'll scroll down to show the new
// comments.
var oldContent = null;
window.setInterval(function () {
    var elem = document.getElementById('chat');
    if (oldContent != elem.innerHTML) {
        scrollToBottom();
    }
    oldContent = elem.innerHTML;
}, 50);

// Scroll to the bottom of the chat window.
function scrollToBottom() {
    var elem = document.getElementById('chat');
    elem.scrollTop = elem.scrollHeight;
}