public class HeavyLifters extends Membros {
    
    

    public HeavyLifters(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
    }

    @Override
    public void postarMensagem() {
        if (SistemaPrincipal.getHorarios() == EnumHorarios.REGULAR){
            System.out.println("Podem contar conosco!\n");
        }
        else if (SistemaPrincipal.getHorarios() == EnumHorarios.EXTRA){
            System.out.println("N00b_qu3_n_Se_r3pita.bat\n");
        }
        
        
    }
    
}
    
