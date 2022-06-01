public class TestDriveArray {
    public static void main(String[] args) {
        //Cria um array de inteiros
        int[] meuArray;
        //Instancia o array
        meuArray = new int[4];
        //Colocando valores no array
        meuArray[0] = 45;
        meuArray[1] = 12;
        meuArray[2] = 9;
        meuArray[3] = 5;

        //Criando um erro
        meuArray[10] = -1;
    }
}