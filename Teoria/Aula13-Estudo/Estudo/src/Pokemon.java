public abstract class Pokemon implements Evoluir{
    private final int numero;
    private final String nome;
    private Status status;

    public Pokemon(int numero, String nome, Status status) {
        this.numero = numero;
        this.nome = nome;
        this.status = status;
    }

    protected void setStatus(Status status) {
        this.status = status;
    }

    public int getNumero(){
        return this.numero;
    }

    public String getNome(){
        return this.nome;
    }

    public Status getStatus(){
        return this.status;
    }

    @Override
    public String toString(){
        return "Pokemon{" +
                "numero=" + numero +
                ", nome='" + nome + '\'' +
                ", status=" + status +
                '}';
    }

    @Override
    public Status somarStatus(Status status1, Status status2) {
        Status retorno = new Status(
            status1.getVida() + status2.getVida(),
            status1.getAtaque() + status2.getAtaque(),
            status1.getDefesa() + status2.getDefesa(),
            status1.getVelocidade() + status2.getVelocidade());
        return retorno;
    }
}