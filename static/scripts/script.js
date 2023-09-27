function copyBTC_ToClipboard() {
    var textToCopy = document.getElementById("btc_addr").innerText;

    var tempTextArea = document.createElement("textarea");
    tempTextArea.value = textToCopy;
    tempTextArea.style.position = "fixed";  // To ensure the textarea is not visible
    document.body.appendChild(tempTextArea);

    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices

    try {
        var successful = document.execCommand("copy");
        var message = successful ? "Bitcoin Address Copied To Clipboard!" : "Unable to copy text.";
        alert(message);
    } catch (error) {
        console.error("Unable to copy text. Error: ", error);
    }

    document.body.removeChild(tempTextArea);
}

function copyETH_ToClipboard() {
    var textToCopy = document.getElementById("eth_addr").innerText;

    var tempTextArea = document.createElement("textarea");
    tempTextArea.value = textToCopy;
    tempTextArea.style.position = "fixed";  // To ensure the textarea is not visible
    document.body.appendChild(tempTextArea);

    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices

    try {
        var successful = document.execCommand("copy");
        var message = successful ? "Ethereum Address Copied To Clipboard!" : "Unable to copy text.";
        alert(message);
    } catch (error) {
        console.error("Unable to copy text. Error: ", error);
    }

    document.body.removeChild(tempTextArea);
}