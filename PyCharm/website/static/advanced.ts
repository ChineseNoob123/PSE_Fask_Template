function typeTest() {
  console.log("Typescript hype");
  fetch("/tstest", {
    method: "POST",
  }).then((_res) => {
    window.location.href = "/";
  });
}

function debug() {
  console.log("Debugging");
  fetch("/debug", {
    method: "POST",
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deleteNote(noteId:number) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
