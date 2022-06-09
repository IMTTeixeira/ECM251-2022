import java.util.ArrayList;
import java.util.List;
public class SistemaPrincipal {
private static EnumHorarios horario;
    public static void run(){
        horario = EnumHorarios.REGULAR;
        
        
        List<Membros> membros = new ArrayList<Membros>();
        membros.add(new MobileMembers("Z3d","Z3d@MAsK_S0c13ty.com",EnumFuncoes.MOBILEMEMBERS));
        membros.add(new HeavyLifters("K4yn","K4yn@MAsK_S0c13ty.com", EnumFuncoes.HEAVYLIFTERS));
        membros.add(new ScriptGuys("V13g0","V13g0@MAsK_S0c13ty.com", EnumFuncoes.SCRIPTGUYS));
        membros.add(new BigBrothers("T4l0n","T4l0n@MAsK_S0c13ty.com",EnumFuncoes.BIGBROTHERS));
        System.out.println("~~~~~~~~~~ Bem-Vindos ao MAsK_S0c13ty ~~~~~~~~~~\n");
        System.out.println("---------- Horário em vigor: " + horario + " ----------\n");
        for (Membros membro : membros) {
            membro.postarMensagem();
        }
        mudarTurno();
        System.out.println("---------- Horário em vigor: " + horario + " ----------\n");
        for (Membros membro : membros) {
            membro.postarMensagem();
        }
        mudarTurno();
        membros.remove(1);
        membros.remove(1);
        System.out.println("---------- Horário em vigor: " + horario + " ----------\n");
        for (Membros membro : membros) {
            membro.postarMensagem();
        }
        System.out.println("~~~~~~> Encerrando Sistema do MAsK_S0c13ty...\n");

        
    }
    public static void mudarTurno(){
        if(horario == EnumHorarios.REGULAR){
            horario = EnumHorarios.EXTRA;
        }
        else if(horario == EnumHorarios.EXTRA){
            horario = EnumHorarios.REGULAR;
        }
    }
    

    public static EnumHorarios getHorarios() {
        return horario;
    }
}
