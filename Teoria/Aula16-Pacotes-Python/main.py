from modelos.documentos import Document, Book, Email
from modelos.plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = Email(to = "luan@eteixeira.com", authors = ['Luan Teixeira'])
    doc3 = Book(title = 'Design Patterns', authors = ['Erich Gamma', 'Richard Helm', 'Ralph Johnson', 'John Vlissides'])
    print(doc2)
    print(doc3)
    

if __name__ == '__main__':
    # planta1 = Arvore('Carvalho')
    # planta2 = Alface(nome = 'Hamburguer de Siri do futuro')

    # print(planta1.ola())
    # print(planta2.ola())
    run_system()