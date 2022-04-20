public class TestDrive{
    public static void executar(){
        System.out.println("Dado Genérico");
        Dado d1 = new Dado("1234");
        System.out.println("Dado criado: " + d1);
        System.out.println("Face Anterior: " + d1.faceAtual());
        //Sorteia uma nova face
        d1.rodar();
        System.out.println("Face Atual: " + d1.faceAtual());

        System.out.println("Dado D6:");
        Dado d2 = new DadoD6("5637");
        System.out.println("Dado criado: " + d2);
        System.out.println("Face Anterior: " + d2.faceAtual());
        //Sorteia uma nova face
        d2.rodar();
        System.out.println("Face Atual: " + d2.faceAtual());

        System.out.println("Dado D10:");
        Dado d3 = new DadoD10("5555");
        System.out.println("Dado criado: " + d3);
        System.out.println("Face Anterior: " + d3.faceAtual());
        //Sorteia uma nova face
        d3.rodar();
        System.out.println("Face Atual: " + d3.faceAtual());

        System.out.println("Dado D20:");
        Dado d4 = new DadoD20("2020");
        System.out.println("Dado criado: " + d4);
        System.out.println("Face Anterior: " + d4.faceAtual());
        //Sorteia uma nova face
        d4.rodar();
        System.out.println("Face Atual: " + d4.faceAtual());
    }
}