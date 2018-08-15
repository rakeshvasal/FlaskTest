from firebase import firebase
firebase = firebase.FirebaseApplication('https://androidone-43cbb.firebaseio.com', None)
result = firebase.get('/users', None)
print (result)
