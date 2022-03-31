public class Conta {
        //Atributos da nossa classe
        private int idConta = 0;
        private double saldo;

        public Conta(String idConta){
            
        }
        public String toString(){
            return "idConta:" + this.idConta;
        }
        //Métodos da classe
    public String visualizarSaldo(){
        return String.format("R$%.2f", saldo);
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
            
        
    }
}
