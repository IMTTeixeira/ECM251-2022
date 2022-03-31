public class Atividade1 {
    public void run(){
                Usuarios usuario = new Usuarios("Luan Teixeira", "12345", "20.01681-6@maua.br");
                Conta c1 = new Conta("123");
                Conta c2 = new Conta("456");
                Conta c3 = new Conta("789");
                
                c1.depositar(1000.0);
                c2.depositar(250.0);
                c3.depositar(3000.0);
    }
       
    
}
