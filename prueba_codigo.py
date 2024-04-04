lista_pendiente = []

def registrar_estudiante(nombre, apellidos, contacto, correo, edad, estrato, sexo, telefono):
    if (sexo == 'masculino' and 15 <= edad <= 25 and estrato in [1, 2]) or (sexo == 'femenino' and 20 <= edad <= 35 and estrato in [1, 2, 3, 4]):
        print(f'Se ha registrado al estudiante {nombre} {apellidos}')
    else:
        lista_pendiente.append(contacto)
        print(f'El estudiante {nombre} {apellidos} no cumple con los criterios y se ha guardado en la lista pendiente')

# Ejemplo de uso
nombre = input('Ingrese el nombre del estudiante: ')
apellidos = input('Ingrese los apellidos del estudiante: ')
contacto = input('Ingrese el contacto del estudiante: ')
correo = input('Ingrese el correo del estudiante: ')
edad = int(input('Ingrese la edad del estudiante: '))
estrato = int(input('Ingrese el estrato del estudiante: '))
sexo = input('Ingrese el sexo del estudiante (masculino o femenino): ')
telefono = input('Ingrese el teléfono del estudiante: ')

registrar_estudiante(nombre, apellidos, contacto, correo, edad, estrato, sexo, telefono)

print('\nContactos pendientes:')
for contacto in lista_pendiente:
    print(f'- {contacto}')



