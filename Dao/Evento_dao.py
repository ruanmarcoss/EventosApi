from Model.Evento import Evento
class EventoDao():
    def __init__(self):
        arquivo = open(r'C:\Users\900160\Documents\EventosApi\Tabela', 'r')
        self.lista = []
        for i in arquivo:
            self.lista.append(i.split(';'))
        arquivo.close()

    def list_all(self):
        lista = []
        for i in self.lista:
            dic = {'ID':i[0],'NOME':i[1],'DATA':i[2],'DESCRICAO':i[3],'LOCAL':i[4]}
        lista.append(dic)
        print(lista)
        return lista




a = EventoDao()
a.list_all()



