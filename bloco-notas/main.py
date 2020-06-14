#Desenvolvido por: Matheus Naranjo
#Linkedin: https://www.linkedin.com/in/matheus-naranjo-35ab22188?originalSubdomain=br
# Ano: 2020
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        #Janela principal
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 524)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowIcon(QtGui.QIcon('images/nota.png'))
        
        #Campo para texto

        self.CampoTexto = QtWidgets.QTextEdit(self.centralwidget) #definindo a construção e o tipo
        self.CampoTexto.setGeometry(QtCore.QRect(0, 0, self.width(), self.height() -43))# determinando a posição e largura X Altura
        #self.CampoTexto.setStyleSheet('background-color: rgb(102, 102, 102);')
        font = QtGui.QFont() #chamando o metodo de fonte
        font.setFamily("Microsoft Sans Serif") #definindo a fonte do Campo Texto como Microsoft Sans Serif
        font.setPointSize(16) #tamanho 12
        self.CampoTexto.setFont(font) #inserindo informações de fonte no CampoTexto
        self.CampoTexto.setObjectName("CampoTexto") # Gerando CampoTexto
        self.CampoTexto.setStyleSheet('background-color: white; color: black;')
        self.CampoTexto.setAcceptRichText(False)
        MainWindow.setCentralWidget(self.centralwidget)

        '''Criando a Menu BAR'''        
        #Barra horrizontal superior com as opções  -  MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow) #definindo a construçao dentro da janela principal
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 25)) # definindo a posição e tamanho(largura e altura)
        self.menubar.setObjectName("menubar") #chamando o objeto
        
        #Menu Arquivo
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        
        #Menu Editar
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")

        #Menu Editar
        self.menuFormatar = QtWidgets.QMenu(self.menubar)
        self.menuFormatar.setObjectName("menuFormatar")

        #Menu Alinhar --> com 4 opções lá dentro, definidas mais abaixo
        self.menuAlinhar = QtWidgets.QMenu(self.menuFormatar)
        self.menuAlinhar.setObjectName("menuAlinhar")

        #Menu Sobre
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")

        #Menu Modo
        self.menuModo = QtWidgets.QMenu(self.menubar)
        self.menuModo.setObjectName("menuModo")

        MainWindow.setMenuBar(self.menubar)
        
        ''' Criando a Status Bar'''
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #self.statusbar.setStyleSheet('background-color: White; color: Black')
        MainWindow.setStatusBar(self.statusbar)


        #DEFININDO AS BARRAS PARA CADA BOTÃO DA MENU BAR
        #Criando a barra de Novo
        self.actionNovo = QtWidgets.QAction(MainWindow)
        self.actionNovo.setObjectName("actionNovo")
        
        #Criando a barra de Salvar
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar.setIcon(QtGui.QIcon('images/save.png'))

        #Criando a barra de Abrir
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionAbrir.setIcon(QtGui.QIcon('images/open.png'))

        #Criando a barra de Copiar
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionCopiar.setIcon(QtGui.QIcon('images/copy.png'))
        #Criando a barra de Colar
        self.actionColar = QtWidgets.QAction(MainWindow)
        self.actionColar.setObjectName("actionColar")
        self.actionColar.setIcon(QtGui.QIcon('images/paste.png'))
        #Criando a barra de Fonte
        self.actionFonte = QtWidgets.QAction(MainWindow)
        self.actionFonte.setObjectName("actionFonte")
        self.actionFonte.setIcon(QtGui.QIcon('images/font.png'))

        #Criando a barra de Centralizar dentro de 'Alinhar'.
        self.actionCentralizar = QtWidgets.QAction(MainWindow)
        self.actionCentralizar.setObjectName("actionCentralizar")
        self.actionCentralizar.setIcon(QtGui.QIcon('images/center.png'))

        #Criando a barra de ajustar à direita dentro de 'Alinhar'.
        self.actionAlinhar_direita = QtWidgets.QAction(MainWindow)
        self.actionAlinhar_direita.setObjectName("actionAlinhar_direita")
        self.actionAlinhar_direita.setIcon(QtGui.QIcon('images/right.png'))

        #Criando a barra de ajustar à esquerda dentro de 'Alinhar'.
        self.actionAlinhar_esquerda = QtWidgets.QAction(MainWindow)
        self.actionAlinhar_esquerda.setObjectName("actionAlinhar_esquerda")
        self.actionAlinhar_esquerda.setIcon(QtGui.QIcon('images/left.png'))

        #Criando a barra de justificar dentro de 'Alinhar'.
        self.actionJustificar = QtWidgets.QAction(MainWindow)
        self.actionJustificar.setObjectName("actionJustificar")
        self.actionJustificar.setIcon(QtGui.QIcon('images/justify.png'))
        
        #opçao de Negrito dentro de FORMATAR
        self.actionNegrito = QtWidgets.QAction(MainWindow)
        self.actionNegrito.setObjectName("actionNegrito")
        self.actionNegrito.setIcon(QtGui.QIcon('images/bold.png'))

        #opçao de Sublinhar dentro de FORMATAR
        self.actionSublinhar = QtWidgets.QAction(MainWindow)
        self.actionSublinhar.setObjectName("actionSublinhar")
        self.actionSublinhar.setIcon(QtGui.QIcon('images/underline.png'))

        #opçao de Itálico dentro de FORMATAR
        self.actionItalico = QtWidgets.QAction(MainWindow)
        self.actionItalico.setObjectName("actionItalico")
        self.actionItalico.setIcon(QtGui.QIcon('images/italic.png'))

        #Opçao de imprimir dentro de Arquivo
        self.actionImprimir = QtWidgets.QAction(MainWindow)
        self.actionImprimir.setObjectName("actionImprimir")
        self.actionImprimir.setIcon(QtGui.QIcon('images/print.png'))

        #Opção de sair dentro de Arquivo
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSair.setIcon(QtGui.QIcon('images/exit.png'))

       #Opção de modo noturno dentro de modo
        self.actionModo_Noturno = QtWidgets.QAction(MainWindow)
        self.actionModo_Noturno.setObjectName("actionModo_Noturno")

        self.actionModo_Noturno1 = QtWidgets.QAction(MainWindow)
        self.actionModo_Noturno1.setObjectName("actionModo_Branco")

        self.actionModo_Noturno2 = QtWidgets.QAction(MainWindow)
        self.actionModo_Noturno2.setObjectName("actionModo_color1")

        self.actionModo_Noturno3 = QtWidgets.QAction(MainWindow)
        self.actionModo_Noturno3.setObjectName("actionModo_color2")

        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName('actionSobre')

        '''Definindo as sub-opções dentro das opções'''
        '''ARQUIVO'''
        #self.menuArquivo.addAction(self.actionNovo) #NOVO dentro de Arquivo
        self.menuArquivo.addAction(self.actionSalvar)#SALVAR dentro de Arquivo
        self.menuArquivo.addAction(self.actionAbrir) #ABRIR dentro de Arquivo
        self.menuArquivo.addAction(self.actionImprimir) #IMPRIMIR dentro de Arquivo
        self.menuArquivo.addAction(self.actionSair) #SAIR dentro de Arquivo

        '''EDITAR'''
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionColar)

        '''ALINHAR'''
        self.menuAlinhar.addAction(self.actionCentralizar)
        self.menuAlinhar.addAction(self.actionAlinhar_direita)
        self.menuAlinhar.addAction(self.actionAlinhar_esquerda)
        self.menuAlinhar.addAction(self.actionJustificar)

        '''FORMATAR'''   
        self.menuFormatar.addAction(self.actionFonte)
        self.menuFormatar.addAction(self.menuAlinhar.menuAction())
        self.menuFormatar.addAction(self.actionNegrito)
        self.menuFormatar.addAction(self.actionSublinhar)
        self.menuFormatar.addAction(self.actionItalico)
    
        '''MODO'''
        self.menuModo.addAction(self.actionModo_Noturno)
        self.menuModo.addAction(self.actionModo_Noturno1)  
        self.menuModo.addAction(self.actionModo_Noturno2)
        self.menuModo.addAction(self.actionModo_Noturno3)

        '''Sobre'''
        self.menuSobre.addAction(self.actionSobre)

    #Nota, a opção sobre não está aqui pois ainda não criei nada pra ela  

        #Adicionando cada ação ao menu bar    
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuFormatar.menuAction())
        self.menubar.addAction(self.menuModo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.titulo_novo = MainWindow.setWindowTitle(_translate("MainWindow", "My notes "))
    
        
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))

        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))

        self.menuFormatar.setTitle(_translate("MainWindow", "Formatar"))

        self.menuAlinhar.setStatusTip(_translate("MainWindow", "Alinhe seu texto"))

        self.menuAlinhar.setTitle(_translate("MainWindow", "Alinhar"))

        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))

        self.menuModo.setTitle(_translate("MainWindow", "Modo"))

        #self.actionNovo.setText(_translate("MainWindow", "Novo"))
        #self.actionNovo.setStatusTip(_translate("MainWindow", "Criar novo Arquivo"))
        self.actionNovo.setShortcut(_translate("MainWindow", "Ctrl+N"))

        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setStatusTip(_translate("MainWindow", "Salvar o arquivo"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))

        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setStatusTip(_translate("MainWindow", "Abrir arquivo"))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        
        self.actionCopiar.setText(_translate("MainWindow", "Copiar"))
        self.actionCopiar.setStatusTip(_translate("MainWindow", "Copiar "))
        self.actionCopiar.setShortcut(_translate("MainWindow", "Ctrl+C"))

        self.actionColar.setText(_translate("MainWindow", "Colar"))
        self.actionColar.setStatusTip(_translate("MainWindow", "Colar"))
        self.actionColar.setShortcut(_translate("MainWindow", "Ctrl+V"))

        self.actionFonte.setText(_translate("MainWindow", "Fonte"))
        self.actionFonte.setStatusTip(_translate("MainWindow", "Altere configurações de formatação"))

        self.actionCentralizar.setText(_translate("MainWindow", "Centralizar"))
        self.actionCentralizar.setStatusTip(_translate("MainWindow", "Texto será centralizado"))
        self.actionCentralizar.setShortcut(_translate("MainWindow", "Ctrl+E"))

        self.actionAlinhar_direita.setText(_translate("MainWindow", "Alinhar à direita"))
        self.actionAlinhar_direita.setStatusTip(_translate("MainWindow", "Alinhe à direita seu texto"))
        self.actionAlinhar_direita.setShortcut(_translate("MainWindow", "Ctrl+G"))

        self.actionAlinhar_esquerda.setText(_translate("MainWindow", "Alinhar à esquerda"))
        self.actionAlinhar_esquerda.setStatusTip(_translate("MainWindow", "Alinhe à esquerda seu texto"))
        self.actionAlinhar_esquerda.setShortcut(_translate("MainWindow", "Ctrl+Q"))

        self.actionJustificar.setText(_translate("MainWindow", "Justificar"))
        self.actionJustificar.setStatusTip(_translate("MainWindow", "Seu texto Justificado"))
        self.actionJustificar.setShortcut(_translate("MainWindow", "Ctrl+J"))

        self.actionNegrito.setText(_translate("MainWindow", "Negrito"))
        self.actionNegrito.setShortcut(_translate("MainWindow", "Ctrl+B"))

        self.actionSublinhar.setText(_translate("MainWindow", "Sublinhar"))
        self.actionSublinhar.setShortcut(_translate("MainWindow", "Ctrl+U"))

        self.actionItalico.setText(_translate("MainWindow", "Itálico"))
        self.actionItalico.setShortcut(_translate("MainWindow", "Ctrl+I"))

        self.actionImprimir.setText(_translate("MainWindow", "Imprimir"))
        self.actionImprimir.setStatusTip(_translate("MainWindow", "Imprima o arquivo"))
        self.actionImprimir.setShortcut(_translate("MainWindow", "Ctrl+P"))

        self.actionSair.setText(_translate("MainWindow", "Sair"))

        self.actionModo_Noturno.setText(_translate("MainWindow", "Modo Dark"))
        self.actionModo_Noturno.setStatusTip(_translate("MainWindow","Escolha o que achar melhor"))
        
        self.actionModo_Noturno1.setText(_translate("MainWindow", "Modo White"))
        self.actionModo_Noturno1.setStatusTip(_translate("MainWindow","Escolha o que achar melhor"))

        self.actionModo_Noturno2.setText(_translate("MainWindow", "Modo color 1"))
        self.actionModo_Noturno2.setStatusTip(_translate("MainWindow","Escolha o que achar melhor"))

        self.actionModo_Noturno3.setText(_translate("MainWindow", "Modo color 2"))
        self.actionModo_Noturno3.setStatusTip(_translate("MainWindow","Escolha o que achar melhor"))

        self.actionSobre.setText(_translate("MainWindow", "Criador"))

        #MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

    def resizeEvent(self, event):
        self.CampoTexto.setGeometry((QtCore.QRect(0,0,self.width(),self.height())))

icon_taskbar = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(icon_taskbar)


#AQUI se importa os sistema operacional, aplica as funções, a classe, execução e opções para sair
'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''