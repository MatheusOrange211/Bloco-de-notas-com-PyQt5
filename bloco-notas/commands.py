from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QApplication, QFontDialog
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from main import Ui_MainWindow

class BlocoWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        self.isItalic = True
        self.isNegrito = True
        self.Issublinhado = True
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.show()
    
        #self.actionNovo.triggered.connect(self.Novo)
        self.actionSalvar.triggered.connect(self.salvar)
        self.actionAbrir.triggered.connect(self.Abrir)
        self.actionImprimir.triggered.connect(self.Imprimir)
        self.actionSair.triggered.connect(self.Sair)


        self.actionCopiar.triggered.connect(self.Copiar)
        self.actionColar.triggered.connect(self.Colar)


        self.actionFonte.triggered.connect(self.Fonte)
        self.actionCentralizar.triggered.connect(self.Centralizar)
        self.actionAlinhar_esquerda.triggered.connect(self.Esquerda)
        self.actionAlinhar_direita.triggered.connect(self.Direita)
        self.actionJustificar.triggered.connect(self.Justificar)
        self.actionNegrito.triggered.connect(self.Negrito)
        self.actionSublinhar.triggered.connect(self.Sublinhado)
        self.actionItalico.triggered.connect(self.Italico)

        self.actionModo_Noturno.triggered.connect(self.Modo)
        self.actionModo_Noturno1.triggered.connect(self.Modo1)
        self.actionModo_Noturno2.triggered.connect(self.Modo2)
        self.actionModo_Noturno3.triggered.connect(self.Modo3)

        self.actionSobre.triggered.connect(self.Sobre)
        

    def Novo(self):
        super().__init__()
        self.setupUi(self)
        self.show()

         #Editar 
        self.actionNovo.triggered.connect(self.Novo)
        self.actionSalvar.triggered.connect(self.salvar)
        self.actionAbrir.triggered.connect(self.Abrir)
        #self.actionImprimir.triggered.connect()
        self.actionSair.triggered.connect(self.Sair)

        #Editar

        self.actionCopiar.triggered.connect(self.Copiar)
        self.actionCopiar.triggered.connect(self.Colar)

    def salvar(self, MainWindow): #Quando digito algo aqui, o texto é salvo!
        self.CampoTexto.setAcceptRichText(False)
        text = BlocoWindow.salvar
        text = self.CampoTexto.toPlainText()
        
        #print(text) --> Fiz isso para ver se o texto realmente era capturado
        #options = QFileDialog.Options() -> isso  aqui era para evitar erros de salvamento, no entanto gerou problemas
        #options |= QFileDialog.DontUseNativeDialog --> isso abria a tela de salvamento do pyqt e nao do windows
        fillename = QFileDialog.getSaveFileName(self, 'Arquivo','Doc',"File Text(*.txt);;Documento Word(*.docx);;Adobe Acrobat (*.pdf);;Html documents (*.html)")[0]
        if fillename:
            with open(fillename,'w') as meu_novo_arquivo:
                meu_novo_arquivo.write(text)
                meu_novo_arquivo.close()
        
        titulo_novo = fillename.split('/')
        titulo_novo = titulo_novo[-1]
        titulo_novo = titulo_novo.split('.txt')
        titulo_novo = titulo_novo[0]
        
        
        
    def Abrir(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self)
        try: 
            file =  open(name[0],'r')
            #print(name[0])
            with file:
                texto = file.read()
                self.CampoTexto.setText(texto)      
        except:
            pass

    def Imprimir(self):
            imprimir = QPrinter(QPrinter.HighResolution)
            previsualizacao = QPrintPreviewDialog(imprimir,self)
            previsualizacao.paintRequested.connect(self.printprevia)
            previsualizacao.exec_()

    def printprevia(self,imprimir):
         self.CampoTexto.print_(imprimir)


    def Sair(self):
        return exit()


    def Copiar(self):  
        self.CampoTexto.copy()
        

    def Colar(self):
        self.CampoTexto.paste()
        self.CampoTexto.setCursor(self.CampoTexto, self.height())


    def Fonte(self):
        fonte, ok = QFontDialog.getFont()
        if ok:
            escolhido = fonte.toString().split(',')
            #print(escolhido)
            #print(escolhido[0])
            #print(escolhido[1])
            #print(escolhido[-1])
            self.CampoTexto.setFontFamily(escolhido[0])
            self.CampoTexto.setFontPointSize(float(escolhido[1]))
            
    def Centralizar(self):
        self.CampoTexto.setAlignment(QtCore.Qt.AlignCenter)

    def Direita(self):
        self.CampoTexto.setAlignment(QtCore.Qt.AlignLeft)

    def Esquerda (self):
        self.CampoTexto.setAlignment(QtCore.Qt.AlignRight)

    def Justificar(self):
        self.CampoTexto.setAlignment(QtCore.Qt.AlignJustify)

    def Negrito(self):
        self.isNegrito = not self.isNegrito
        if self.isNegrito is False:
            self.CampoTexto.setFontWeight(QtGui.QFont().Bold)
        else:
            self.CampoTexto.setFontWeight(QtGui.QFont().Bold is False)

    def Sublinhado(self):
        self.Issublinhado = not self.Issublinhado

        return self.CampoTexto.setFontUnderline(self.Issublinhado)

    def Italico(self):
        self.isItalic = not self.isItalic
        return self.CampoTexto.setFontItalic(self.isItalic) 
      

    def Modo(self):
        self.CampoTexto.setStyleSheet('background-color: #222831; color: #a7d129;')
        self.statusbar.setStyleSheet('background-color: #222831; color: #a7d129;')
    def Modo1(self):
        self.CampoTexto.setStyleSheet('background-color: white; color: black;')
        self.statusbar.setStyleSheet('background-color: White; color: Black;')
    def Modo2(self):
        self.CampoTexto.setStyleSheet('background-color: #222831; color: #00fff5;')
        self.statusbar.setStyleSheet('background-color: #222831; color: #00fff5;')
    def Modo3(self):
        self.CampoTexto.setStyleSheet('background-color: #222831; color: #f6c90e;')
        self.statusbar.setStyleSheet('background-color: #222831; color: #f6c90e;')
        
    def Sobre(self):
        self.tela = QtWidgets.QMessageBox()
        self.tela.setWindowIcon(QtGui.QIcon('images/nota.png'))
        self.tela.setWindowTitle('MyNotes - Sobre este programa')
        self.tela.setText('Desenvolvido por Matheus Naranjo para fins de estudo.\nAgradeço em especial a meu amigo Ozeias Sousa,\nCuja ajuda foi fundamental\n\nGados dos Zodíaco® - 2020')
        self.tela.exec_()