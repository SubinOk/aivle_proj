idx = 2
function AddFile(){
    document.getElementById('file-cnt').value = idx

    const new_field = document.getElementById('file-field-clone').cloneNode(true);
    new_field.childNodes[1].childNodes[3].setAttribute('name', "files"+idx)
    new_field.childNodes[3].childNodes[1].setAttribute('name', "answer"+idx)

    const obj = document.getElementById("file-field");
    obj.appendChild(new_field)

    idx += 1
}