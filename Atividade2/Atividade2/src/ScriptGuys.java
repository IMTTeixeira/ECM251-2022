public class ScriptGuys extends Membros {

    

    public ScriptGuys(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
    }

    @Override
    public void postarMensagem() {
        if (SistemaPrincipal.getHorarios() == EnumHorarios.REGULAR){
            System.out.println("Prazer em ajudar novos amigos de código!\n");
        }
        else if (SistemaPrincipal.getHorarios() == EnumHorarios.EXTRA){
            System.out.println("QU3Ro_S3us_r3curs0s.py\n");
        }
        
        
    }
    
}
    
