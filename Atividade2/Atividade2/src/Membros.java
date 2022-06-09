public abstract class Membros implements PostarMensagem{
    private String nome;
    private String email;
    private EnumFuncoes funcao;
   
    
    public Membros(String nome, String email, EnumFuncoes funcao) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
    }
    
    public String getNome() {
        return nome;
    }
    public String getEmail() {
        return email;
    }
    public EnumFuncoes getFuncao() {
        return funcao;
    }
    
    @Override
    public String toString() {
        return "Members [email=" + email + ", funcao=" + funcao + ", nome=" + nome + "]";
    }
   
}