function copyEncryptedData() {
    let text = document.getElementById("encData").value;
    navigator.clipboard.writeText(text)
    .then(() => {
        alert('Text copied to clipboard');
    })
    .catch(err => {
        alert('Error in copying text: ', err);
    });
}


function copyDecryptionKey() {
    /* Get the text field */
    let text = document.getElementById('d_key').value;

    navigator.clipboard.writeText(text)
    .then(() => {
        alert('Text copied to clipboard');
    })
    .catch(err => {
        alert('Error in copying text: ', err);
    });
}

function copyDecryptedData() {
    /* Get the text field */
    let text = document.getElementById('decryptedData').value;
    
    navigator.clipboard.writeText(text)
    .then(() => {
        alert('Text copied to clipboard');
    })
    .catch(err => {
        alert('Error in copying text: ', err);
    });
}