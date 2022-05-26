public class Bebida extends Produto{
    private final int volume;
    private final EnumTemperatura temperatura;
    private final EnumAlergias alergia;
    private final EnumTiposBebida tipo;
    public Bebida(double preco, int quantidade, String descricao, String nome, int volume, EnumTemperatura temperatura,
            EnumAlergias alergia, EnumTiposBebida tipo) {
        super(preco, quantidade, descricao, nome);
        this.volume = volume;
        this.temperatura = temperatura;
        this.alergia = alergia;
        this.tipo = tipo;
    }
    public int getVolume() {
        return volume;
    }
    public EnumTemperatura getTemperatura() {
        return temperatura;
    }
    public EnumAlergias getAlergias() {
        return alergia;
    }
    public EnumTiposBebida getTipos() {
        return tipo;
    }
    @Override
    public double gerarPrecoComDesconto() {
        return getPreco()*0.90;
    }
     
}
