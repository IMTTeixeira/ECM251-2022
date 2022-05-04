import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    protected String tipo;
    protected static int id;
    protected double valorHora;
   
    public Veiculo(String id, double valorHora, String tipo) {
        this.tipo = tipo;
        this.valorHora = valorHora;
    }
    public String getTipo() {
        return tipo;
    }
    public double getValorHora() {
        return valorHora;
    }
    public static String gerarId(){
        id = ThreadLocalRandom.current().nextInt(10000,100000);
        return String.format("id = %i", id);
    }
     @Override
    public String toString() {
        return "Veículo [tipo=" + tipo + ", id=" + id + ", Valor/hora=" + valorHora + "]";
    }
}
