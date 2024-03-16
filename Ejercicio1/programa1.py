import threading
import os

#Función para el hilo 1
def task1():
    print("Tarea 1 asignada al thread: {}".format(threading.current_thread().name))
    print("ID del hilo corriendo la tarea 1 {}:".format(threading.current_thread().ident))

#Función para el hilo 2
def task2():
    print("Tarea 2 asignada al thread: {}".format(threading.current_thread().name))
    print("ID del hilo corriendo la tarea 2 {}:".format(threading.current_thread().ident))

#Aunque ya sabemos que este es el programa principal,
#ejemplificamos el uso de la variable __name__
if __name__ == "__main__":
    print("ID del proceso corriendo el programa main: {}".format(os.getpid))
    print("ID del identificador del hilo corriendo el programa main: {}".format(threading.current_thread().ident))
    print("Nombre del Main thread: {}".format(threading.current_thread().name))

#Creamos los hilos
t1 = threading.Thread(target=task1, name="Hilo 1")
t2 = threading.Thread(target=task2, name="Hilo 2")

#Iniciamos los hilos
t1.start()
t2.start()

#Terminamos los hilos
t1.join()
t2.join()

print ("Programa terminado!")







