const imageElement = document.getElementById('uploadedImage');
const fileInputElement = document.querySelector("input[type=file]")

function readURL(e) {

  if (e.target.files && e.target.files[0]) {
    let reader = new FileReader();
        console.log('start');
    reader.onload = function(e) {
        imageElement.setAttribute('src', reader.result);
    }

    reader.readAsDataURL(e.target.files[0]);
  }
}

fileInputElement.addEventListener('change', readURL);
