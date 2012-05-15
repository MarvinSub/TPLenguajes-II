#Programa escrito en Python 2.5
#Elaborado por: Erick Monge Angulo
#		Rafael Oliver Murillo
#		Marvin Suarez Benson		


from pyswip import * #Se importa la libreria pyswip que permitirá la interconexión
from string import upper

p = Prolog() #variable utilizada para hacer las consultas de prolog

def salir():  # para salir del programa

	while True:
		salir=raw_input("Desea hacer otra operacion[S/N]: ")
		salir=upper(salir)
		if salir=="S" or salir=="SI":			
			return 0
		elif salir=="N" or salir=="NO":			
			validacion=1
			return 1
		else:
			print "Favor indique SI o NO"

def verif_otra(a):
	verif_otra=0 #indica  si se elige una opcion valida en la pregunta de si desea otrao consulta
		     # 0 indica que no fue correcta, 1 lo contrario
	while True:
		if a==1:
			otra_cons=raw_input("Desea hacer otra consulta [S/N]: ")
		else:
			otra_cons=raw_input("Desea hacer otro registro [S/N]: ")
		otra_cons=upper(otra_cons)
		if otra_cons=="N" or otra_cons=="NO":
			return 1
		elif otra_cons=="S" or otra_cons=="SI":
			return 0
		else:
			print"Favor elija SI o NO"

def realizar_consulta(Nombre, Genero, Raza, Edad, Ecosistema, Comida, lista_param, lista_var2):
	q = Query(animal(Nombre, Genero, Raza, Edad, Ecosistema, Comida), module=animal_modulo) #realiza la consulta a la base de conocimientos
	cont=0#indica si hubieron resultados de la consulta, cont=0 indica que no hubo resultados, cont>0 lo contrario.
	o=0#lleva el indice de la lista_var2
	while q.nextSolution():

		cont+=1
		for e in lista_param: #imprime la lista de los parametros del animal
			print e

		for i in lista_var:				
			print lista_var2[o]+str(i.value) #imprime los resultados de los animales encontrados 
			o+=1 #para verificar si obtuvo resultados
		o=0
		print"\n"
	if cont==0:
		print "Su busqueda no obtuvo resultados, pruebe con otras caracteristicas"
	q.closeQuery() #se cierra la consulta





print "Bienvenido a ZooSystem\n"


validacion=0 #valida hasta que se cierre el programa 

assertz = Functor("assertz")
animal = Functor("animal", 6) #functor de las caracteristicas de los animales
animal_modulo = newModule("animal_modulo")

#ejemlos estaticos para la realización de consultas
call(assertz(animal("LUNA", "HEMBRA", "PERRO", "8", "CASA", "EUKA")), module=animal_modulo)
call(assertz(animal("NALA", "HEMBRA", "PERRO", "6", "CASA", "HUESO")), module=animal_modulo)

while validacion==0:

	eleccion=raw_input("\nQue desea hacer:\n\na.Consultas\nb.Mantenimiento\nc.Salir\nDigite su eleccion: ")
	eleccion= upper(eleccion)
	ind_gen=0
	otra_con=0#indica si se desea hacer una consulta, 1 indica no se quiere hacer otra, 0 lo contrario
	if eleccion=="A":  

		print "\n\nBienvenido al sistema de consultas\n\n"
		
		while otra_con==0: #ciclo del modo consulta
			lista_var=[]#contiene las variables que no se especificaron y se usaran en prolog
			lista_var2=[]#contiene el nombre del campo que repesenta cada variable
			lista_param=[]#contiene la informacion que brindo el usuario en la consulta
			
			completa=raw_input("Que tipo de consulta desea hacer: \n\na.Por parametros\nb.Total\nIndique la opcion: ")
			print ""
			#imprime todos los animeales
			if completa=="b" or completa=="B":
				print "Animales Actualmente registrados en el zoologico.\n"
				Nombre=Variable()
				lista_var.append(Nombre)
				lista_var2.append("Nombre: ")
			
				Genero=Variable()
				lista_var.append(Genero)
				lista_var2.append("Genero: ")

				Raza=Variable()
				lista_var.append(Raza)
				lista_var2.append("Raza: ")
				
				Edad=Variable()
				lista_var.append(Edad)
				lista_var2.append("Edad: ")

				Ecosistema=Variable()
				lista_var.append(Ecosistema)
				lista_var2.append("Ecosistema: ")

				Comida=Variable()
				lista_var.append(Comida)
				lista_var2.append("Comida favorita: ")			

				realizar_consulta(Nombre, Genero, Raza, Edad, Ecosistema, Comida, lista_param, lista_var2) 
				otra_con=verif_otra(1)
			elif completa=="a" or completa=="A":
				#de entrada las caractristicas de los animales y de salida los animales encontrados
				ind_gen=0
				print "Indique las caracteristicas del animal que desea indentificar:\n *Recuerde que si no conoce una caracteristica simplemente la deja en blanco\n"

				# en cada if se obtiene la inforamcion que el usuario digita, si no digita nada se pasa el campo a las 					listas que guardan
				# las variables de prolog
				nombre= raw_input ("Nombre: ")
				if nombre=="":
					Nombre=Variable()
					lista_var.append(Nombre)
					lista_var2.append("Nombre: ")
				else:
					Nombre=upper(nombre)
					lista_param.append("Nombre: "+str(Nombre))
				print "Genero: \na.Hembra\nb.Macho\n"
		
				while ind_gen==0:
				
						genero= raw_input ("Indique genero: ")
						genero=upper(genero)
						if genero=="A":
							ind_gen=1
							genero="HEMBRA"
							Genero=genero
							lista_param.append("Genero: "+str(Genero))
						elif genero=="B":
							ind_gen=1
							genero="MACHO"
							Genero=genero
							lista_param.append("Genero: "+str(Genero))
						elif genero=="":
							ind_gen=1
							Genero=Variable()
							lista_var.append(Genero)
							lista_var2.append("Genero: ")
						else:
							print "Favor Digite A , B o dejar vacio"

				raza= raw_input ("Raza: ")
				if raza=="":
					Raza=Variable()
					lista_var.append(Raza)
					lista_var2.append("Raza: ")
				else:
					Raza=upper(raza)
					lista_param.append("Raza: "+str(Raza))

				edad=raw_input("Edad: ")
				if edad=="":
					Edad=Variable()
					lista_var.append(Edad)
					lista_var2.append("Edad: ")
				else:
					Edad=upper(edad)
					lista_param.append("Raza: "+ str(Edad))

				ecosistema=raw_input ("Ecosistema: ")
				if ecosistema=="":
					Ecosistema=Variable()
					lista_var.append(Ecosistema)
					lista_var2.append("Ecosistema: ")
				else:
					Ecosistema=upper(ecosistema)
					lista_param.append("Ecosistema: "+str(Ecosistema))

				comida_fav= raw_input ("Comida favorita: ")
				if comida_fav=="":
					Comida=Variable()
					lista_var.append(Comida)
					lista_var2.append("Comida favorita: ")
				else:
					Comida=upper(comida_fav)
					lista_param.append("Comida favorita: "+str(Comida))
			
				print "\nLa busqueda se hizo bajo los siguientes parametros:\n"

				#se imprimen primero los datos en los que se baso la busqueda
				for i in lista_param:
					print i
				print "\nLos resultados de la consulta son: \n"
				realizar_consulta(Nombre, Genero, Raza, Edad, Ecosistema, Comida, lista_param, lista_var2) 	
				otra_con=verif_otra(1)
			else:
				print "Digite una opcion valida\n"
		validacion = salir()

	elif eleccion=="B": #modo mantenimiento
		reg_otro=0
		print "\n\nBienvenido al sistema de mantenimiento\n\n"
		while reg_otro==0: #para el ingreso de los datos de los animales
			print "\nIndique los datos del nuevo animal por registrar\n"
			ind_gen=0
			while ind_gen==0:			
				nombre_reg= raw_input ("Nombre: ")
				if nombre_reg=="" or nombre_reg==" ":
					print "\nFavor ingrese un nombre valido\n"
				else:
					ind_gen=1
			ind_gen=0
			print "Genero: \na.Hembra\nb.Macho\n"
			while ind_gen==0:				
				genero_reg= raw_input ("Digite genero: ")
				genero_reg=upper(genero_reg)
				if genero_reg=="A":
					ind_gen=1
					genero_reg="Hembra"
				elif genero_reg=="B":
					ind_gen=1
					genero_reg="Macho"
				else:
					print "Favor Digite A o B"
			ind_gen=0
			while ind_gen==0:			
				raza_reg= raw_input ("Raza: ")
				if raza_reg=="" or raza_reg==" ":
					print "Favor ingrese una raza valida"
				else:
					ind_gen=1
			
			ind_gen=0
			while ind_gen==0:
				edad_reg=raw_input("Edad: ")
				if edad_reg=="" or edad_reg==" ":
					print "Favor ingrese una edad valida"
				else:
					ind_gen=1
				
			ind_gen=0
			while ind_gen==0:			
				eco_reg=raw_input ("Ecosistema: ")
				if eco_reg=="" or eco_reg==" ":
					print "Favor ingrese un ecosistema valido"
				else:
					ind_gen=1
			ind_gen=0
			while ind_gen==0:			
				comida_reg= raw_input ("Comida favorita: ")
				if comida_reg=="" or comida_reg==" ":
					print "Favor ingrese una comida valida"
				else:
					ind_gen=1			

			#crea el nuevo hecho en la base de conocimiento de prolog
			call(assertz(animal(upper(nombre_reg), upper(genero_reg), upper(raza_reg), upper(edad_reg), upper(eco_reg), upper(comida_reg))), 			module=animal_modulo)

			print "\nHa registrado un animal en zoologico con las siguientes caracteristicas:\n"
			print "Nombre: "+str(nombre_reg)+"\ngenero: "+str(genero_reg)+"\nRaza: "+str(raza_reg)+"\nEdad: "+str(edad_reg)+"\nEcosistema: "+str	(eco_reg)+"\nComida favorita: "+str(comida_reg)

			reg_otro=verif_otra(2)

			

		validacion=salir() #valida si se desea salir
				
	elif eleccion=="C":
		exit()  #se sale del programa

	else:
		print "Favor indique A, B o C\n"

