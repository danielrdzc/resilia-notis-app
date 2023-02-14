import firebase from 'firebase/app'
import 'firebase/messaging'

var firebaseConfig = {
    apiKey: "AIzaSyCf0QMmF7yBPoWXwTKo9nSyPqyXEDl-0cE",
    authDomain: "wisptest-91d06.firebaseapp.com",
    projectId: "wisptest-91d06",
    storageBucket: "wisptest-91d06.appspot.com",
    messagingSenderId: "375844969034",
    appId: "1:375844969034:web:0cb39902ecc49dab3d64b3",
    measurementId: "G-4NKF7ER5LS"
}

firebase.initializeApp(firebaseConfig)

export default firebase.messaging()