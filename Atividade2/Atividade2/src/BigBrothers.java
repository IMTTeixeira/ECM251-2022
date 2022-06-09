public class BigBrothers extends Membros {

    public BigBrothers(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
    }

    @Override
    public void postarMensagem() {
        if (SistemaPrincipal.getHorarios() == EnumHorarios.REGULAR){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!\n");
        }
        else if (SistemaPrincipal.getHorarios() == EnumHorarios.EXTRA){
            System.out.println("...\n");
        }
        
        
    }
    
    
}