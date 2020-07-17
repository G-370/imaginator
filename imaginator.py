from libs.imagine import Imagine
import sys 
import os.path

#testObj = Imagine("libs\\imagine.py", 50, 50)

def pegarCaminho():
	caminho = input("> ")
	if not ( os.path.exists(caminho) ) and not ( caminho == "SAIR" ):
		raise ValueError( str(caminho) + " <- Isso não é um caminho válido. \n")
	return caminho

def funçãoPrincipal(caminho):
	imaginate = Imagine(caminho)
	imaginate.constructRawArray()
	imaginate.makeRGBPixelArray()
	imaginate.makeImage()
	imaginate._image.save( os.path.basename(caminho) + ".png")
	print("Sucesso!\n Para continuar, digite outro caminho. Se quiser sair, digite SAIR")

def execInterativa():
	print((30*"~") + "\n" + "|Imaginator versão 0.1|\n Utiliza Pillow e Imagine \n Programado por GALEW \n" + (30 * "~") + "\n")
	print("Digite o caminho para o arquivo:\n")
	caminho = pegarCaminho()
	funçãoPrincipal(caminho)
	if caminho == "SAIR":
		exit()
	looping = True
	while(looping):
			caminho = pegarCaminho()
			if caminho == "SAIR":
				exit()
			funçãoPrincipal(caminho)


if ( sys.argv[1] == "executar"):
	execInterativa()


if (__name__ == "__main__"):
	print(sys.argv)

	if len(sys.argv) != 2 :
		raise TypeError("Falta argumento, " + "você me deu " + str((len(sys.argv) - 1)) + ", preciso de ao menos 1 argumento.")

	if not ( os.path.exists(sys.argv[1]) ):
		raise ValueError("O primeiro" + str(sys.argv[1]) + " argumento não é um caminho.")

	testObj = Imagine(sys.argv[1])
	testObj.constructRawArray()
	testObj.makeRGBPixelArray()
	testObj.makeImage()

	#saveFile = open("theFile.txt", mode="wb")
	#saveFile.write(testObj._pixelArray)
	#saveFile.close()
	testObj._image.save( os.path.basename(sys.argv[1]) + ".png")