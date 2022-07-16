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


/* Creating a function that will create an alert message. */
const alertPlaceholder = document.getElementById('liveAlertPlaceholder');

const alertUser = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    alertUser('If in the encrypted data you encounter the symbol "", please refresh the page to re-encrypt!', 'danger')
  })
}