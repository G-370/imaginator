from PIL import Image
#from array import array

class Imagine:
    _rawArray = bytearray()
    _pixelArray = bytearray()
    _width = int()
    _height = int()

    def __init__(self, inputFile):
        if(type(inputFile) != str):
            raise TypeError("O caminho para o arquivo deve ser uma string.")

        with open(inputFile, 'r') as file:
            self._inputFile = file.readlines()

        for i in range(0, len(self._inputFile) - 1):
            self._inputFile[i] = self._inputFile[i].rstrip("\n")

        #DEBUG
        #print("\n\n" + "Input File" + "\n" + 150 * "-" + "\n\n" + str(self._inputFile) + "\n\n" + 150 * "-")

    def calculateDimensions(self):
        linesizes = list()
        linecount = int()
        for line in self._inputFile:
            linesizes.append(len(line))# - 1)
            linecount += 1
        self._width = max(linesizes)
        self._height = linecount

    def setDimensions(self, x, y):
        self._width = x
        self._height = y

    def padAmount(self, toPad, padAsChar=32):
        for i in range(1, toPad):
            self._rawArray.append(padAsChar) ## The character used to pad, default is [space], ASCII 32.

    def constructRawArray(self):

        self.calculateDimensions()

        for line in self._inputFile:

            for x in line:
                if ( x == "\n"):
                    self._rawArray.append(50)
                else:
                    self._rawArray.append(ord(x))   ## Research what the ord function does

            if ( len(line) < self._width ):
                toPad = self._width - len(line) +1
                self.padAmount(toPad)
                #print(x)
        #self._inputFile.seek(0) #Return the current line number to zero so as not to break future iterations over it.
        
        #DEBUG
        #print( "\n\n\n" + "Raw Array" + "\n" + str(self._rawArray) + "\n\n" + 150 * "-")

    def makeRGBPixelArray(self):
        for bytePos in range(0, (len(self._rawArray))):
            self._pixelArray.append(self._rawArray[bytePos])
            self._pixelArray.append(self._rawArray[bytePos])
            self._pixelArray.append(self._rawArray[bytePos])
            #self._pixelArray.append(100)
            #self._pixelArray.append(0)

        #DEBUG
        #print("\n\n\n" + "Pixel Array" + "\n" + str(self._pixelArray) + "\n\n" + 150 * "-")

    def makeImage(self):
        pass
        #<--------- Down here adds 2 new attributes!!! --------->#
        #self._imageConstructor = Image.new('RGB', (self._width, self._height))     # self._pixelArray
        #self._image = Image.frombytes( "RGB", ((self._width-1)*3 , self._height*3 ), bytes(self._pixelArray), "raw", "RGB", 0, 1 )
        self._image = Image.frombytes( "RGB", (self._width , self._height) , bytes(self._pixelArray), "raw", "RGB", 0, 1 )
        #self._image = self._image.transpose(Image.FLIP_LEFT_RIGHT)
        self._image = self._image.resize((self._width * 10 , self._height * 10), 0)