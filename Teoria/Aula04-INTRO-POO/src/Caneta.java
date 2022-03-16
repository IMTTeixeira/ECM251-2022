public class Caneta {
    //Caracteristica da caneta - seus atributos
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int carga_maxima = 100; //Valor em porcentagem

    //Comportamentos das canetas - seus Métodos
    void escrever(String texto){
        for(int i = 0; i<texto.length(); i++){  //for para verificar se a carga é suficiente para o texto
            if(carga>0){
                System.out.print(texto.charAt(i));
                carga = carga -1;
            } else{
                System.out.println("Caneta sem carga.");
                break;
            }
        }       
        System.out.println();
    }

    //função para iniciar um objeto caneta
    void iniciarCaneta(String modelo, String cor, double ponta){
        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;
        this.carga = carga_maxima;
    }

    String pegarDados(){
        return "Modelo:" + modelo +
        "\nCor:" + cor +
        "\nPonta:" + ponta +
        "\nCarga:" + carga;

    }

}
