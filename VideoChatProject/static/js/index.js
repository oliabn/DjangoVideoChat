console.log('index.js has run');

let usernameInput = document.querySelector('#username'); 
let btnJoin = document.querySelector('#btn-join');

let username;

let webSocket;

function webSocketOnMessage(event) {
    let parsedData = JSON.parse(event.data);
    let message = parsedData['message'];

    console.log('message: ', message);
}

// on click btnJoin
btnJoin.addEventListener('click', () => {
    username = usernameInput.value;

    console.log('username: ', username);

    if(username == '') {
        return;
    }

    usernameInput.value = '';
    usernameInput.disabled = true;
    usernameInput.style.visibility = 'hidden';

    btnJoin.disabled = true;
    btnJoin.style.visibility = 'hidden';

    let labelUsername = document.querySelector('#label-username');
    labelUsername.innerHTML = username;

    let location = window.location;
    let wsStsrt = 'ws://';
    if(location.protocol == 'https:') {
        wsStsrt = 'wss://;'
    }

    let endPoint = wsStsrt + location.host + location.pathname;

    console.log('endPoint: ', endPoint);

    // webSocet object
    webSocket = new WebSocket(endPoint);

    webSocket.addEventListener('open', (e) => {
        console.log('Connection opened');

        let jsonStr = JSON.stringify({'message': 'This is a message',});
        webSocket.send(jsonStr);
    });

    webSocket.addEventListener('message', webSocketOnMessage);
 
    webSocket.addEventListener('close', (e) => {
        console.log('Connection closed');
    });
    webSocket.addEventListener('error', (e) => {
        console.log('Error occured');
    });

});

let localStreem = new MediaStream();

// const constraints = {
//     'video': true, 
//     'audio': true 
// };

// const localVideo = document.querySelector('#local-video');
// console.log(localVideo);

// let userMedia = navigator.mediaDevices.getUserMedia(constraints).then(stream => {
//     localStreem = stream;
//     localVideo.strObject = localStreem;
//     localVideo.muted = true;
// })
// .catch(error =>{
//     console.log('Error accessing media devices.', error);
// });

async function playVideoFromCamera() {
    try {
        const constraints = {'video': true, 'audio': true};
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        const videoElement = document.querySelector('#local-video');
        console.log(videoElement)
        videoElement.srcObject = stream;
    } catch(error) {
        console.error('Error opening video camera.', error);
    }
}

playVideoFromCamera();
