public class Aplicacao{
    public static void run(){
        Usuario usuario1 = new Usuario(Usuario.getNome());
        Carro carro = new Carro(Carro.gerarId(), 100.0, "Carro");
        Moto moto = new Moto(Moto.gerarId(), 50.0, "Moto");
        Patinete patinete = new Patinete(Patinete.gerarId(), 10.0, "Patinete");
        Bicicleta bicicleta = new Bicicleta(Bicicleta.gerarId(), 20.0, "Bicicleta");
    }

}