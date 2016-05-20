from flask import Flask, request, render_template
#from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def cargar():
	print 'Entro en cargar'
	return render_template('index.html')

@app.route('/', methods=['POST'])
def obtener(): 
	print "ENTRO en obtener"
	#os.system('analyze -f /usr/local/share/freeling/config/es.cfg tagged < /var/www/html/input.txt > /var/www/html/output.txt')
	#return 'hola mundo'
	texto=str(request.form['id_entrada'])
	print ("HOLA MUNDO!: ", texto)
	escribirArchivo(texto)
	analisis_morfo=leerArchivo()
	print(analisis_morfo)
	return render_template('index.html', texto=texto, texto_analisis=analisis_morfo)

def escribirArchivo(cadena):
	file=open("entrada.txt", "w")
	file.write(cadena)
	file.close()
	os.system('analyze -f /usr/local/share/freeling/config/es.cfg tagged < entrada.txt > salida.txt')

def leerArchivo():
	file=open("salida.txt", "r")
	morfo=""
	for line in file:		
		morfo+=line
	return morfo


if __name__ == '__main__': 
	app.run()
