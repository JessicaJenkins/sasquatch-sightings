window.ajaxSuccess = function () {
  response = JSON.parse(this.responseText);
  document.getElementById('uploaded').setAttribute("src", response["secure_url"]);
}

window.AJAXSubmit = function (formElement) {
  console.log("starting AJAXSubmit");
  if (!formElement.action) { return; }
  let xhr = new XMLHttpRequest();
  xhr.onload = ajaxSuccess;
  xhr.open("post", "https://api.cloudinary.com/v1_1/seeking-sasquatch/image/upload");
  xhr.send(new FormData(formElement));
}