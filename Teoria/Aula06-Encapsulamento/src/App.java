public class App {
    public static void main(String[] args) throws Exception {
        Cliente c1 = new Cliente("Luan Teixeira", 
            "480.623.388-94", 
            "20.01681-6@maua.br", 
            new Conta(12345)
        );
        
        System.out.println("Nome do cliente:" + c1.getNome());
        System.out.println("E-mail do cliente:" + c1.getEmail());
        System.out.println("CPF do cliente:" + c1.getCpf());
        c1.getConta().visualizarSaldo();
    }
}
