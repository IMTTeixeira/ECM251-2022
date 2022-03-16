public class App {
    public static void main(String[] args) {
        //Declara um objeto caneta e instancia ele
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("BIC", "Azul", 2.0);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Stabilo", "Vermelha", 0.4);

        c1.escrever("O hashira do Som é o brabo, mas não é o melhor hashira. Contudo ninguém nega que o Muzan parece o Michael Jackson");
        c2.escrever("Qual é o melhor hashira? P.S: O do vento");
        
    }
}
