import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
        //Cria um ArrayList para as Canetas
        ArrayList<Caneta> canetas = new ArrayList<Caneta>();
        //Adiciona as canetas
        canetas.add(new Caneta("Azul", 0.7));
        canetas.add(new Caneta("Vermelha", 1.0));
        
        //Estudo do método size()
        System.out.println("Tamanho do ArrayList agora: " + canetas.size());

        canetas.remove(0);
        System.out.println("Tamanho do ArrayList agora: " + canetas.size());

        //Passar por todos os elementos do ArrayList
        //Método 1
        System.out.println("Método 1: For do C");
        for(int i = 0; i < canetas.size(); i++) {
            System.out.println("Cor da caneta: " + canetas.get(i).cor);
        }
        //Método 2
        System.out.println("Método 2: Foreach do Java");
        for (Caneta caneta : canetas) {
            System.out.println("Cor da caneta: " + caneta.cor);
        }
    }
}
