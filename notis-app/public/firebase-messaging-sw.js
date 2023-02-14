importScripts('https://www.gstatic.com/firebasejs/8.2.7/firebase-app.js')
importScripts('https://www.gstatic.com/firebasejs/8.2.7/firebase-messaging.js')

const firebaseConfig = {
    apiKey: "AIzaSyCf0QMmF7yBPoWXwTKo9nSyPqyXEDl-0cE",
    authDomain: "wisptest-91d06.firebaseapp.com",
    projectId: "wisptest-91d06",
    storageBucket: "wisptest-91d06.appspot.com",
    messagingSenderId: "375844969034",
    appId: "1:375844969034:web:0cb39902ecc49dab3d64b3",
    measurementId: "G-4NKF7ER5LS"
};

const app = firebase.initializeApp(firebaseConfig)

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler((payload) => {
    console.log('noti');

    const title = 'test';
    const options = {
        body: 'asdsad'
    };

    return self.registration.showNotification(title, options);
})