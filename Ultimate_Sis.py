#ALUNO: ÂNGELO LUIS MARCELINO DO NASCIMENTO SILVA, ADS,201916360020
import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QPushButton,QMainWindow
from PySide2.QtCore import QFile
from PySide2 import QtGui
from PySide2 import QtCore
import mysql.connector

#Apenas Banco===================================================================
meu_banco=("sistema_comercial",)

def conecta_banco(db=None):
    if db == None:
        banco=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
        )
        return banco
    else:
        banco=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=db
        )
        return banco

def existe_banco():
    status=False
    try:
        db=conecta_banco()
        cursor=db.cursor()
        cursor.execute("SHOW DATABASES")
        for banco in cursor:
            #print(banco)
            if banco == meu_banco:
                status=True
                return status
                #print(status)


        cursor.close()
        db.close()
    except BaseException as erro:
        print("Erro ao verificar banco"+str(erro))
    #finally:


def cria_banco():
    try:
        db=conecta_banco()
        cursor=db.cursor()
        cursor.execute("CREATE DATABASE "+meu_banco[0])
        cria_tabelas()
    except BaseException as erro:
        print("Erro ao criar banco"+str(erro))
    finally:
        cursor.close()
        db.close()

def cria_tabelas():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY,login VARCHAR(30),senha VARCHAR(30))"
        cursor.execute(sql)
        sql=sql="CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255),endereco VARCHAR(255),ddd VARCHAR(12),tel INT(20),email VARCHAR(255))"
        cursor.execute(sql)
        sql="CREATE TABLE produtos (id INT AUTO_INCREMENT PRIMARY KEY,produto VARCHAR(255),quantidade INT(255),valor VARCHAR(255))"
        cursor.execute(sql)
        val=("admin","admin")
        sql="INSERT INTO usuarios (login,senha) VALUES (%s,%s)"
        cursor.execute(sql,val)
        db.commit()
    except BaseException as erro:
        print("Erro ao criar tabelas..."+str(erro))
    finally:
        cursor.close()
        db.close()

#Classes========================================================================
class janela_principal():
    janela=None
    def __init__(self):
        global janela
        #self.jan=QtGui.qApp
        self.arquivo=QFile("janela_principal.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        janela=self.carrega.load(self.arquivo)
        self.arquivo.close()
        janela.show()

        janela.setFixedSize(700,500)
        janela.btn_cadastrar_cliente.clicked.connect(jan_cad_cliente)
        janela.btn_cadastrar_produto.clicked.connect(conecta_cad_pro)
        janela.btn_sair.clicked.connect(sai_sis)
        janela.btn_lista_clientes.clicked.connect(jan_list_cliente)
        janela.btn_lista_produtos.clicked.connect(jan_list_produto)
        janela.btn_pesquisar_cliente.clicked.connect(jan_pesq_cliente)
        janela.btn_pesquisar_produto.clicked.connect(jan_pesq_produto)
        janela.btn_excluir_cliente.clicked.connect(janelinha_excluir_cliente)
        janela.btn_excluir_produto.clicked.connect(janelinha_excluir_produto)
        janela.btn_editar_produto.clicked.connect(janelinha_editar_produto)
        janela.btn_editar_cliente.clicked.connect(janelinha_editar_cliente)

class janela_cad_cliente():
    jan_cad_cli=None
    def __init__(self):
        global jan_cad_cli
        #self.cad_cli=QtGui.qApp
        self.arquivo=QFile("cadastrar_cliente.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_cad_cli=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_cad_cli.show()

        jan_cad_cli.setFixedSize(700,500)
        jan_cad_cli.btn_limpar.clicked.connect(botao_limparr)
        jan_cad_cli.btn_cadastrar.clicked.connect(botao_cadastrar_cliente)
        jan_cad_cli.btn_voltar.clicked.connect(sai_cadcliente)

class janela_cad_produto():
    jan_cad_pro=None
    def __init__(self):
        global jan_cad_pro
        #self.cad_pro=QtGui.qApp
        self.arquivo=QFile("cadastrar_produto.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_cad_pro=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_cad_pro.show()

        jan_cad_pro.setFixedSize(700,500)
        jan_cad_pro.btn_voltar_cadas_produto.clicked.connect(sai_cad_pro)
        jan_cad_pro.btn_limpar_cadas_produto.clicked.connect(limpar_cad_pro)
        jan_cad_pro.btn_cadastrar_cadas_produto.clicked.connect(cad_produto)

class janela_lista_clientes():
    jan_list_cli=None
    def __init__(self):
        global jan_list_cli
        #self.list_cli=QtGui.qApp
        self.arquivo=QFile("lista_clientes.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_list_cli=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_list_cli.show()

        jan_list_cli.setFixedSize(700,500)
        jan_list_cli.btn_sair_list_cli.clicked.connect(sai_jan_list_cli)
        jan_list_cli.btn_gerar_list_cli.clicked.connect(gera_lista_cli)

class janela_lista_produtos():
    jan_list_pro=None
    def __init__(self):
        global jan_list_pro
        #self.list_pro=QtGui.qApp
        self.arquivo=QFile("lista_produtos.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_list_pro=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_list_pro.show()

        jan_list_pro.setFixedSize(700,500)
        jan_list_pro.btn_sair_list_pro.clicked.connect(sai_lista_pro)
        jan_list_pro.btn_gerar_list_pro.clicked.connect(gera_lista_pro)

class janela_pesquisar_cliente():
    jan_pesq_cli=None
    def __init__(self):
        global jan_pesq_cli
        #self.pesq_cli=QtGui.qApp
        self.arquivo=QFile("pesquisar_cliente.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_pesq_cli=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_pesq_cli.show()

        jan_pesq_cli.setFixedSize(700,500)
        jan_pesq_cli.btn_voltar.clicked.connect(sai_jan_pesq_cli)
        jan_pesq_cli.btn_pesquisar_nome.clicked.connect(gera_pesquisa_nome)
        jan_pesq_cli.btn_pesquisar_endereco.clicked.connect(gera_pesquisa_endereco)

class janela_pesquisar_produto():
    jan_pesq_pro=None
    def __init__(self):
        global jan_pesq_pro
        #self.pesq_pro=QtGui.qApp
        self.arquivo=QFile("pesquisar_produto.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_pesq_pro=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_pesq_pro.show()

        jan_pesq_pro.setFixedSize(700,500)
        jan_pesq_pro.btn_voltar_pesq_prod.clicked.connect(sai_jan_pesq_pro)
        jan_pesq_pro.btn_pesquisar_produto.clicked.connect(gera_pesquisa_produto)#Passou
        jan_pesq_pro.btn_pesquisar_valor.clicked.connect(gera_pesquisa_valor)

class janela_excluir_cliente():
    jan_excluir_cli=None
    def __init__(self):
        global jan_excluir_cli
        #self.pesq_pro=QtGui.qApp
        self.arquivo=QFile("excluir_cliente.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_excluir_cli=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_excluir_cli.show()

        jan_excluir_cli.setFixedSize(700,500)
        jan_excluir_cli.btn_sair_excluir_cli.clicked.connect(sai_excluir_cli)
        jan_excluir_cli.btn_pesquisar.clicked.connect(pesquisa_cliente_excluir)
        jan_excluir_cli.btn_excluir.clicked.connect(exclui_cli_definitivo)

class janela_excluir_produto():
    jan_excluir_pro=None
    def __init__(self):
        global jan_excluir_pro
        #self.pesq_pro=QtGui.qApp
        self.arquivo=QFile("excluir_produto.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_excluir_pro=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_excluir_pro.show()

        jan_excluir_pro.setFixedSize(700,500)
        jan_excluir_pro.btn_sair_excluir_pro.clicked.connect(sai_excluir_pro)
        jan_excluir_pro.btn_pesquisar_produto.clicked.connect(pesquisa_produto_excluir)
        jan_excluir_pro.btn_excluir_produto.clicked.connect(exclui_pro_definitivo)

class janela_editar_produto():
    jan_editar_pro=None
    def __init__(self):
        global jan_editar_pro
        #self.edit_pro=QtGui.qApp
        self.arquivo=QFile("editar_produto.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_editar_pro=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_editar_pro.show()

        jan_editar_pro.setFixedSize(700,500)
        jan_editar_pro.btn_sair_editar_produto.clicked.connect(sai_editar_produto)
        jan_editar_pro.btn_pesquisar_produtos.clicked.connect(pesquisando_produtos_edit)
        jan_editar_pro.btn_editar_referencia.clicked.connect(editando_referencia_produto)
        jan_editar_pro.btn_editar_quantidade.clicked.connect(editando_qntd_produto)
        jan_editar_pro.btn_editar_valor.clicked.connect(editando_valor_produto)
        jan_editar_pro.btn_confirmar_editar_pro.clicked.connect(confirmandoeditpro)

class janela_editar_cliente():
    jan_editar_cli=None
    def __init__(self):
        global jan_editar_cli
        #self.edit_pro=QtGui.qApp
        self.arquivo=QFile("editar_cliente.ui")
        self.arquivo.open(QFile.ReadOnly)
        self.carrega=QUiLoader()
        jan_editar_cli=self.carrega.load(self.arquivo)
        self.arquivo.close()
        jan_editar_cli.show()

        jan_editar_cli.setFixedSize(700,500)
        jan_editar_cli.btn_sair_editar_cliente.clicked.connect(sai_editar_cliente)
        jan_editar_cli.btn_editar_nome.clicked.connect(editando_nome_cliente)
        jan_editar_cli.btn_editar_endereco.clicked.connect(editando_endereco_cliente)
        jan_editar_cli.btn_pesquisar_clientes.clicked.connect(pesquisando_clientes_edit)
        jan_editar_cli.btn_confirmar_editar_cli.clicked.connect(confirmando_cliente_editar)

#Funções de Chamada e Saída=====================================================
def jan_pri():
    window.close()
    a=janela_principal()

def jan_cad_cliente():
    janela.close()
    a=janela_cad_cliente()

def sai_sis():
    janela.close()

def conecta_cad_pro():
    janela.close()
    janela_cad_produto()

def sai_cadcliente():
    jan_cad_cli.close()
    a=janela_principal()

def sai_cad_pro():
    jan_pri()
    jan_cad_pro.close()

def jan_list_cliente():
    janela.close()
    a=janela_lista_clientes()

def jan_list_produto():
    janela.close()
    a=janela_lista_produtos()

def sai_jan_list_cli():
    jan_pri()
    jan_list_cli.close()

def sai_lista_pro():
    jan_pri()
    jan_list_pro.close()

def jan_pesq_cliente():
    janela.close()
    a=janela_pesquisar_cliente()

def sai_jan_pesq_cli():
    jan_pri()
    jan_pesq_cli.close()

def jan_pesq_produto():
    janela.close()
    a=janela_pesquisar_produto()

def sai_jan_pesq_pro():
    jan_pri()
    jan_pesq_pro.close()

def janelinha_excluir_cliente():
    a=janela_excluir_cliente()
    janela.close()

def sai_excluir_cli():
    jan_pri()
    jan_excluir_cli.close()

def janelinha_excluir_produto():
    a=janela_excluir_produto()
    janela.close()

def sai_excluir_pro():
    jan_pri()
    jan_excluir_pro.close()

def janelinha_editar_produto():
    a=janela_editar_produto()
    janela.close()

def sai_editar_produto():
    jan_pri()
    jan_editar_pro.close()

def janelinha_editar_cliente():
    a=janela_editar_cliente()
    janela.close()

def sai_editar_cliente():
    jan_pri()
    jan_editar_cli.close()

#Funções Interativas/Botões=====================================================
def botao_entrar():
    lg=str(window.txt_login.text())
    sn=str(window.txt_senha.text())
    try:
        loogin=False
        senhaa=False
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="SELECT * FROM usuarios"#botao_entrar
        cursor.execute(sql)
        resultado=cursor.fetchall()
        for r in resultado:#r1 == login r2==senha
            if r[1] == lg:
                loogin=True
            if r[2] == sn:
                senhaa=True
        if loogin and senhaa == True:
            window.label_resposta.setText("Logado com Sucesso...")
            jan_pri()#Primeiro chama a jan pri Para depois fechar >>)))
            window.close()
        else:
            window.label_resposta.setText("Login ou Senha incorretos")
    except:
        print("Erro no botão entrar de login")
    finally:
        cursor.close()
        db.close()

def botao_limpar():
    try:
        window.txt_login.setText("")
        window.txt_senha.setText("")
        window.label_resposta.setText("")
    except:
        print("Erro no botão limpar")

def botao_limparr():
    try:
        jan_cad_cli.txt_nome.setText("")
        jan_cad_cli.txt_endereco.setText("")
        jan_cad_cli.txt_telefone.setText("")
        jan_cad_cli.txt_email.setText("")
        jan_cad_cli.txt_ddd.setText("")
        jan_cad_cli.lbl_clientecadastrado.setText("")
    except:
        print("Erro no botão limpar")

def limpar_cad_pro():
    try:
        jan_cad_pro.txt_produto.setText("")
        jan_cad_pro.txt_qtd_produto.setText("")
        jan_cad_pro.txt_valor.setText("")
        jan_cad_pro.lbl_produto_cadastrado.setText("")
    except:
        print("Erro ao limpar cadastro de Produto...")

def botao_cadastrar_cliente():
    try:
        bugiganga=True
        nm=jan_cad_cli.txt_nome.text()
        end=jan_cad_cli.txt_endereco.text()
        ddd=int(jan_cad_cli.txt_ddd.text())
        tel=int(jan_cad_cli.txt_telefone.text())
        email=jan_cad_cli.txt_email.text()
        if nm == "":
            bugiganga=False
        elif end == "":
            bugiganga=False
        elif end == "":
            bugiganga=False
        elif tel == "":
            bugiganga=False
        elif email == "":
            bugiganga=False
        bimba=0
        for arroba in email:
            if arroba == "@":
                bimba=bimba+1
        if bimba == 0:
            bugiganga=False
        xaxa=".com"
        if xaxa not in email:
            bugiganga=False
        if ddd < 10:
            bugiganga=False
        if tel < 9999999:
            bugiganga=False
        jan_cad_cli.lbl_clientecadastrado.setText("Preencha todos os campos corretamente...")
        if bugiganga == True:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="INSERT INTO clientes (nome, endereco, ddd, tel, email) VALUES (%s, %s, %s, %s, %s)"
            val=(nm,end,ddd,tel,email)
            cursor.execute(sql,val)
            db.commit()
            jan_cad_cli.lbl_clientecadastrado.setText("Cliente Cadastrado com Sucesso.")
    except BaseException as erro:
        jan_cad_cli.lbl_clientecadastrado.setText("Preencha todos os campos corretamente...")
        print("Erro ao cadastrar cliente..."+str(erro))
    finally:
        cursor.close()
        db.close()

def cad_produto():
    try:
        lasanha=True
        pro=jan_cad_pro.txt_produto.text()
        qnt=int(jan_cad_pro.txt_qtd_produto.text())
        valor=float(jan_cad_pro.txt_valor.text())
        if qnt == 0:
            lasanha=False
        if len(pro) < 2:
            lasanha=False
        elif pro == "":
            lasanha=False
        if lasanha == True:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="INSERT INTO produtos (produto, quantidade, valor) VALUES (%s, %s, %s)"
            val=(pro,qnt,valor)
            cursor.execute(sql,val)
            db.commit()
            jan_cad_pro.lbl_produto_cadastrado.setText("Produto Cadastrado com Sucesso...")
        else:
            jan_cad_pro.lbl_produto_cadastrado.setText("Preencha todos os campos corretamente...")
    except:
        jan_cad_pro.lbl_produto_cadastrado.setText("Preencha todos os campos corretamente...")
    finally:
        cursor.close()
        db.close()

def gera_lista_cli():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="SELECT * FROM clientes"
        cursor.execute(sql)
        resultado=str(cursor.fetchall())
        jan_list_cli.label_lista_cli.setText(resultado)
    except:
        print("Erro ao gerar lista CLIENTES...")
    finally:
        cursor.close()
        db.close()

def gera_lista_pro():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="SELECT * FROM produtos"
        cursor.execute(sql)
        resultado=str(cursor.fetchall())
        jan_list_pro.label_lista_pro.setText(resultado)
    except:
        print("Erro ao gerar lista de Produtos...")
    finally:
        cursor.close()
        db.close()

def gera_pesquisa_nome():
    jan_pesq_cli.lbl_alerta.setText("")
    qq=True
    a=jan_pesq_cli.txt_nome_ou_endereco.text()
    if a == "":
        qq=False
    if qq == False:
        jan_pesq_cli.lbl_alerta.setText("Preencha o campo acima")
    if qq == True:
        try:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="SELECT * FROM clientes WHERE nome LIKE '%"+a+"%'"
            cursor.execute(sql)
            resultado=str(cursor.fetchall())
            jan_pesq_cli.lbl_resultado_pesquisa.setText(resultado)
        except:
            jan_pesq_cli.lbl_alerta.setText("Preencha corretamente")
            print("Erro ao gerar pesquisa CLIENTE...")
        finally:
            cursor.close()
            db.close()

def gera_pesquisa_endereco():
    jan_pesq_cli.lbl_alerta.setText("")
    qq=True
    a=jan_pesq_cli.txt_nome_ou_endereco.text()
    if a == "":
        qq=False
    if qq == False:
        jan_pesq_cli.lbl_alerta.setText("Preencha o campo acima")
    if qq == True:
        try:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="SELECT * FROM clientes WHERE endereco LIKE '%"+a+"%'"
            cursor.execute(sql)
            resultado=str(cursor.fetchall())
            jan_pesq_cli.lbl_resultado_pesquisa.setText(resultado)
        except:
            jan_pesq_cli.lbl_alerta.setText("Preencha corretamente")
            print("Erro ao gerar pesquisa CLIENTE...")
        finally:
            cursor.close()
            db.close()

def gera_pesquisa_produto():
    jan_pesq_pro.lbl_alerta_produto_valor.setText("")
    qq=True
    a=jan_pesq_pro.txt_produto_valor.text()
    if a == "":
        qq=False
    if qq == False:
        jan_pesq_pro.lbl_alerta_produto_valor.setText("Preencha o campo acima")
    if qq == True:
        try:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="SELECT * FROM produtos WHERE produto LIKE '%"+a+"%'"
            cursor.execute(sql)
            resultado=str(cursor.fetchall())
            jan_pesq_pro.lbl_resultado_pesquisa_produto.setText(resultado)
        except:
            jan_pesq_pro.lbl_alerta_produto_valor.setText("Preencha o campo acima")
            print("Erro ao gerar pesquisa CLIENTE...")
        finally:
            cursor.close()
            db.close()

def gera_pesquisa_valor():
    jan_pesq_pro.lbl_alerta_produto_valor.setText("")
    qq=True
    a=jan_pesq_pro.txt_produto_valor.text()
    if a == "":
        qq=False
    if qq == False:
        jan_pesq_pro.lbl_alerta_produto_valor.setText("Preencha o campo acima")
    if qq == True:
        try:
            db=conecta_banco(meu_banco[0])
            cursor=db.cursor()
            sql="SELECT * FROM produtos WHERE valor LIKE '%"+a+"%'"
            cursor.execute(sql)
            resultado=str(cursor.fetchall())
            jan_pesq_pro.lbl_resultado_pesquisa_produto.setText(resultado)
        except:
            jan_pesq_pro.lbl_alerta_produto_valor.setText("Preencha o campo acima")
            print("Erro ao gerar pesquisa CLIENTE...")
        finally:
            cursor.close()
            db.close()

def pesquisa_cliente_excluir():
    try:
        jan_excluir_cli.lbl_excluido.setText("")
        ab=jan_excluir_cli.txt_nome.text()
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql = 'SELECT * FROM clientes WHERE nome=%s'
        val=(ab,)
        cursor.execute(sql,val)
        resultado =str(cursor.fetchall())
        if resultado == "[]":
            jan_excluir_cli.lbl_cliente_completo.setText("Nada encontrado...")
        else:
            jan_excluir_cli.lbl_cliente_completo.setText(resultado)
            a=resultado[1]
    except:
        jan_excluir_cli.lbl_cliente_completo.setText("Fracassei")
    finally:
        cursor.close()
        db.close()

def exclui_cli_definitivo():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        abobora=True
        ab=jan_excluir_cli.txt_nome.text()
        if ab == "":
            abobora=False
            jan_excluir_cli.lbl_excluido.setText("Insira o cliente...")
        if abobora==True:
            sql = 'SELECT * FROM clientes WHERE nome=%s'
            val=(ab,)
            cursor.execute(sql,val)
            resultado =str(cursor.fetchall())
            if ab in resultado:
                sql = "DELETE FROM clientes WHERE clientes.nome = %s "
                val=(ab,)
                cursor.execute(sql,val)
                db.commit()
                jan_excluir_cli.lbl_excluido.setText("Excluido com sucesso...")
            else:
                jan_excluir_cli.lbl_excluido.setText("Cliente não encontrado...")
    except:
        print("Erro")
    finally:
        cursor.close()
        db.close()

def pesquisa_produto_excluir():
    try:
        jan_excluir_pro.lbl_excluido.setText("")
        ab=jan_excluir_pro.txt_produto.text()
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql = 'SELECT * FROM produtos WHERE produto=%s'
        val=(ab,)
        cursor.execute(sql,val)
        resultado =str(cursor.fetchall())
        if resultado == "[]":
            jan_excluir_pro.lbl_produto_completo.setText("Nada encontrado...")
        else:
            jan_excluir_pro.lbl_produto_completo.setText(resultado)
    except:
        jan_excluir_pro.lbl_produto_completo.setText("Fracassei")
    finally:
        cursor.close()
        db.close()

def exclui_pro_definitivo():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        abobora=True
        ab=jan_excluir_pro.txt_produto.text()
        if ab == "":
            abobora=False
            jan_excluir_pro.lbl_excluido.setText("Insira o produto...")
        if abobora==True:
            sql = 'SELECT * FROM produtos WHERE produto=%s'
            val=(ab,)
            cursor.execute(sql,val)
            resultado =str(cursor.fetchall())
            if ab in resultado:
                sql = "DELETE FROM produtos WHERE produtos.produto = %s "
                val=(ab,)
                cursor.execute(sql,val)
                db.commit()
                jan_excluir_pro.lbl_excluido.setText("Excluido com sucesso...")
            else:
                jan_excluir_pro.lbl_excluido.setText("Produto não encontrado...")
    except:
        print("Erro")
    finally:
        cursor.close()
        db.close()

def editando_nome_cliente():
    try:
        abobora=True
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        r=jan_editar_cli.txt_cliente_procurado.text()
        newname=jan_editar_cli.txt_alteracao_cliente.text()
        if len(newname) > 0:
            sql="UPDATE clientes SET nome = %s WHERE nome = %s"
            val=(newname,r)
            cursor.execute(sql,val)
            db.commit()
            jan_editar_cli.lbl_resultado_final_cliente.setText("Nome alterado com sucesso...")
        else:
            jan_editar_cli.lbl_resultado_final_cliente.setText("Preencha o nome acima...")
    except:
        jan_editar_cli.lbl_resultado_final_cliente.setText("Erro...")
    finally:
        cursor.close()
        db.close()

def editando_endereco_cliente():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        rr=jan_editar_cli.txt_cliente_procurado.text()
        enderecco=jan_editar_cli.txt_alteracao_cliente.text()
        if len(enderecco) > 0 :
            sql = "SELECT * FROM clientes WHERE nome LIKE '%"+rr+"%'"
            cursor.execute(sql)
            resultado=cursor.fetchone()
            a=str(resultado[2])
            #print(a)
            sql="UPDATE clientes SET endereco = %s WHERE endereco = %s"
            val=(enderecco,a)
            cursor.execute(sql,val)
            db.commit()
            jan_editar_cli.lbl_resultado_final_cliente.setText("Endereço Alterado com sucesso...")
        else:
            jan_editar_cli.lbl_resultado_final_cliente.setText("Preencha o endereço acima...")
    except:
        jan_editar_cli.lbl_resultado_final_cliente.setText("Erro ao editar endereço...")
    finally:
        cursor.close()
        db.close()

def pesquisando_clientes_edit():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="SELECT * FROM clientes"
        cursor.execute(sql)
        resultado=str(cursor.fetchall())
        jan_editar_cli.txt_lista_clientes.setText(resultado)
    except:
        jan_editar_cli.lbl_encontrou_ou_n_cliente.setText("Erro ao pesquisar...")
        print("Erro ao gerar lista CLIENTES...")
    finally:
        cursor.close()
        db.close()

def confirmando_cliente_editar():
    try:
        zzz=jan_editar_cli.txt_cliente_procurado.text()
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql = 'SELECT * FROM clientes WHERE nome=%s'
        val=(zzz,)
        cursor.execute(sql,val)
        resultado=str(cursor.fetchall())
        if zzz in resultado:
            jan_editar_cli.lbl_encontrou_ou_n_cliente.setText(resultado)
        else:
            jan_editar_cli.lbl_encontrou_ou_n_cliente.setText("Cliente não encontrado...")
    except:
        print("Erro ao confirmar cliente editar")
    finally:
        cursor.close()
        db.close()

def editando_referencia_produto():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        rr=jan_editar_pro.txt_produto_procurado.text()
        newref=jan_editar_pro.txt_alteracao.text()
        if len(newref) > 0 :
            sql = "SELECT * FROM produtos WHERE produto LIKE '%"+rr+"%'"
            cursor.execute(sql)
            resultado=cursor.fetchone()
            a=str(resultado[1])
            #print(a)
            sql="UPDATE produtos SET produto = %s WHERE produto = %s"
            val=(newref,a)
            cursor.execute(sql,val)
            db.commit()
            jan_editar_pro.lbl_resultado_final_produto.setText("Ref  Alterada com sucesso...")
        else:
            jan_editar_pro.lbl_resultado_final_produto.setText("Preencha a ref acima...")
    except:
        jan_editar_pro.lbl_resultado_final_produto.setText("Erro ao editar referencia prod...")
    finally:
        cursor.close()
        db.close()

def editando_qntd_produto():
    try:
        bolala=True
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        rr=jan_editar_pro.txt_produto_procurado.text()
        newqntd=jan_editar_pro.txt_alteracao.text()
        #print(type(newqntd))
        #print(newqntd,'NOVO')
        q=("a" ,"b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p" ,"q", "r", "s", "t", "u", "v", "w", "x" ,"y" ,"z")
        qq=("A" ,"B", "C" ,"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ,"P" ,"Q", "R", "S", "T", "U", "V", "W", "X" ,"Y" ,"Z")
        for a in newqntd:
            if a  in q :
                bolala=False
                #print("Tenho Minusculas")
        for a in newqntd:
            if a in qq:
                bolala=False
                #print("Maiusculas")
        if len(newqntd) <= 0:
            bolala=False


        if bolala == True:
            sql = "SELECT * FROM produtos WHERE produto LIKE '%"+rr+"%'"
            cursor.execute(sql)
            resultado=cursor.fetchone()
            a=str(resultado[2])
            #print(a)
            sql="UPDATE produtos SET quantidade = %s WHERE quantidade = %s"
            val=(newqntd,a)
            cursor.execute(sql,val)
            db.commit()
            jan_editar_pro.lbl_resultado_final_produto.setText("Quantidade Alterada com sucesso...")
        else:
            jan_editar_pro.lbl_resultado_final_produto.setText("Preencha a quantidade acima...")
    except:
        jan_editar_pro.lbl_resultado_final_produto.setText("Erro ao editar Quantidade prod...")
    finally:
        cursor.close()
        db.close()

def editando_valor_produto():
    try:
        blue=True

        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        rr=jan_editar_pro.txt_produto_procurado.text()
        newvalor=jan_editar_pro.txt_alteracao.text()

        z=("a" ,"b", "c" ,"d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o" ,"p" ,"q", "r", "s", "t", "u", "v", "w", "x" ,"y" ,"z")
        zz=("A" ,"B", "C" ,"D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ,"P" ,"Q", "R", "S", "T", "U", "V", "W", "X" ,"Y" ,"Z")
        for zzz in newvalor:
            if zzz in z:
                blue=False
                #print("Tenho minusculas")
            if zzz in zz:
                blue=False
                #print("Tenho maiusuclas")

        if newvalor <= "0":
            blue=False
            jan_editar_pro.lbl_resultado_final_produto.setText("Insira um Valor maior...")
            #print("Quero ser maior!!")


        if blue == True:
            sql = "SELECT * FROM produtos WHERE produto LIKE '%"+rr+"%'"
            cursor.execute(sql)
            resultado=cursor.fetchone()
            a=str(resultado[3])
            #print(a)

            sql="UPDATE produtos SET valor = %s WHERE valor = %s"
            val=(newvalor,a)
            cursor.execute(sql,val)
            db.commit()
            jan_editar_pro.lbl_resultado_final_produto.setText("Valor Alterado com sucesso...")
        else:
            jan_editar_pro.lbl_resultado_final_produto.setText("Preencha o Valor acima...")
    except:
        jan_editar_pro.lbl_resultado_final_produto.setText("Erro ao editar Valor prod...")
    finally:
        cursor.close()
        db.close()

def pesquisando_produtos_edit():
    try:
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql="SELECT * FROM produtos"
        cursor.execute(sql)
        resultado=str(cursor.fetchall())
        jan_editar_pro.txt_lista_produtos.setText(resultado)
    except:
        jan_editar_pro.lbl_encontrou_ou_n_produto.setText("Erro ao pesquisar...")
        print("Erro ao gerar lista produtos...")
    finally:
        cursor.close()
        db.close()

def confirmandoeditpro():
    try:
        yyy=jan_editar_pro.txt_produto_procurado.text()
        db=conecta_banco(meu_banco[0])
        cursor=db.cursor()
        sql = 'SELECT * FROM produtos WHERE produto=%s'
        val=(yyy,)
        cursor.execute(sql,val)
        resultado=str(cursor.fetchall())
        if yyy in resultado:
            jan_editar_pro.lbl_encontrou_ou_n_produto.setText(resultado)
        else:
            jan_editar_pro.lbl_encontrou_ou_n_produto.setText("Produto não encontrado...")
    except:
        print("Erro ao confirmar Produto editar")
    finally:
        cursor.close()
        db.close()





if __name__ == "__main__":
    if not existe_banco():
        cria_banco()
    else:
        q=["login.ui"]
        app=QApplication(sys.argv)
        ui_file=QFile(q[0])
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        window.show()

        #jan_pri()
        window.setFixedSize(700,500)
        window.btn_entrar.clicked.connect(botao_entrar)
        window.btn_limpar.clicked.connect(botao_limpar)

        sys.exit(app.exec_())







#
