

public class Caneta {
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_MAXIMA = 100; // HOJE o final é const (criar constante)
    
    void escrever(String texto){
        for (int i = 0;i < texto.length();i++){
            if(carga>0){
                System.out.print(texto.charAt(i));
                carga -= 1;
            } else{
                System.out.println("\nCANETA SEM CARGA");
                break;
            }
        }
        System.out.println();
    }
    void iniciarCaneta(String modelo,String cor,double ponta){
        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;
        this.carga = CARGA_MAXIMA; // valor da carga em porcentagem
    }

    String pegarDados(){
        return "Modelo: " + modelo +
        "\n-Cor : "+ cor +
        "\n-Ponta : "+ ponta +
        "\n-Carga : "+ carga;
    }
}
