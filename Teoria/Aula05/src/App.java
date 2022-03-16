public class App {
    public static void main(String[] args) throws Exception {
        //declara um objeto caneta e instancia ele
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("BIC", "Azul", 1.0);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Stabillo", "Vermelha", 0.4);
        
        c1.escrever("O hashira do som é um cara pica, mas n é o melhor Hashira, contudo ninguem nega que o Musan, parece o Michael Jackson");
        c2.escrever("Qual é o melhor?");
        

        
    }
}
