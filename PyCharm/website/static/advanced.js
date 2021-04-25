function typeTest() {
    console.log("Typescript hype");
    fetch("/tstest", {
        method: "POST"
    }).then(function (_res) {
        window.location.href = "/";
    });
}
function debug() {
    console.log("Debugging");
    fetch("/debug", {
        method: "POST"
    }).then(function (_res) {
        window.location.href = "/";
    });
}
function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId })
    }).then(function (_res) {
        window.location.href = "/";
    });
}
