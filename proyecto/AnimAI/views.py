from django.shortcuts import render
from django.contrib import messages
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth
from .models import MiModelo
from .forms import userForm
from .forms import loginForm
from .forms import testUser
from pyrebase import pyrebase
from django.template import RequestContext

firebaseConfig = {
  "apiKey": "AIzaSyCRw5jZZPvmdA3TgP_jRnuUHp_Y92to9Ew",
  "authDomain": "anim-ai-13c1d.firebaseapp.com",
  "databaseURL": "https://anim-ai-13c1d-default-rtdb.firebaseio.com",
  "projectId": "anim-ai-13c1d",
  "storageBucket" : "anim-ai-13c1d.appspot.com",
  "messagingSenderId" : "508533010561",
  "appId": "1:508533010561:web:3600df94f907b6be7bdd80",
  "measurementId": "G-KMK4THVYBZ"
}

try:
    firebase = pyrebase.initialize_app(config=firebaseConfig)
    print("firebase going")
except:
    print("not cant")
authen = firebase.auth()


cred = credentials.Certificate("C:/Users/USUARIO/Downloads/V5/V2/TSWIII/proyecto/AnimAI/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def index(request):
    objetos = MiModelo.objects.all()
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                emailS = data['email']
                passwordS = data['contraseña']  # Utilizar 'contraseña' en lugar de 'password'
                
                user = authen.sign_in_with_email_and_password(emailS, passwordS)
                print(user["idToken"])
                testF = testUser()
                response = render(request,'inicio.html', {"form" : testF})
                print("hereeee")
                response.set_cookie('idToken', user["idToken"])
                print()
                print("here")   
                
                # strg = firebase.storage()
                # strg.child("img").put("C:/Users/User/Desktop/V2/TSWIII/proyecto/AnimAI/atras.jpg")
                print("signIn good")
                return response
            except:
                print("signIn Bad")
                pass
        else:  # Si el formulario no es válido, volver a renderizar el formulario con los errores
            return render(request, 'index.html', {'form': form, 'objetos': objetos})
    else:
        form = userForm()  # Crear un formulario vacío si el método de solicitud es GET
    return render(request, 'index.html', {'form': form, 'objetos': objetos})


def insertIntoFirestore(id, data):
    db = firestore.client()
    print("db client")
    docRef = db.collection("USUARIOS")
    docRef.add(data,id)

def getIdUser(emailU):
    user = auth.get_user_by_email(emailU)
    print(user.uid + " es")
    print()
    return user.uid



def registrarme(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nameI = data['nombre']
            lastnameI = data['apellido']
            emailI = data['email']
            passwordI = data['contraseña']
            cellphoneI = data['telefono']
            try:
                authen.create_user_with_email_and_password(nameI,lastnameI,emailI,passwordI,cellphoneI)
                db = firestore.client()
                collUsuarios = db.collection("USUARIOS")
                collUsuarios.add({"nombre" : nameI, "apellido" : lastnameI, "email" : emailI, "contraseña" : passwordI, "telefono" : cellphoneI})
                print("here")
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')  # Muestra un mensaje de éxito
                form = loginForm()  # Limpia el formulario
            except Exception as e:
                messages.error(request, f'Error al registrar usuario: {e}')  # Muestra un mensaje de error
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')  # Muestra un mensaje de error si el formulario no es válido
            return render(request, 'registrarme.html', {'form': form})
    else:
        form = loginForm()
    return render(request, 'registrarme.html', {'form': form})

def inicio(request):
    if request.method == 'POST':
        print("request POST")
        form = testUser(request.POST,request.FILES)
        
        if (form.is_valid()):
            print("ist")
            data = form.cleaned_data
            name = data['title']
            file = request.FILES['file']
            print("fil")
            strg = firebase.storage()
            print("fill")
            strg.child(name).put(file)
        else:
            print("notis")
    
    else:
        form = testUser()
        print("get")
    
    print("here is the request ")
    return render(request, 'inicio.html', {'form': form})




def configuracion(request):
    objetos = MiModelo.objects.all()
    return render(request, 'configuracion.html', {'objetos': objetos})

def cuenta(request):
    objetos = MiModelo.objects.all()
    return render(request, 'cuenta.html', {'objetos': objetos})

def historial(request):
    objetos = MiModelo.objects.all()
    return render(request, 'historial.html', {'objetos': objetos})

