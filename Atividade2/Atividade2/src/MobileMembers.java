public class MobileMembers extends Membros {

   

    public MobileMembers(String nome, String email, EnumFuncoes funcao) {
        super(nome, email, funcao);
    }

    @Override
    public void postarMensagem() {
        if (SistemaPrincipal.getHorarios() == EnumHorarios.REGULAR){
            System.out.println("Happy Coding!\n");
        }
        else if (SistemaPrincipal.getHorarios() == EnumHorarios.EXTRA){
            System.out.println("Happy_C0d1ng. Maskers\n");
        }
        
        
    }
}
