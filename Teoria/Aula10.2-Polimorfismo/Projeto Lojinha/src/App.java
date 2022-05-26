public class App {
    public static void main(String[] args) throws Exception {
        Produto manga = new Literatura(29.9, 10, "Foda pa baralho", "One Piece", "TOEI", "Eichiro Oda", 100, EnumGeneroLiteratura.ACAO);
        Produto coca = new Bebida(10.0, 10, "Bonzao", "Coca", 500, EnumTemperatura.FRIO, EnumAlergias.CORANTE, EnumTiposBebida.REFRIGERANTE);
        Produto tepokki = new Comida(10, 20, "Sei la", "Tepokki", 150.0, "Coréia", EnumAlergias.GLUTEN, EnumTiposComida.SALGADA);
        
        System.out.println("Preços Regulares: ");
        System.out.println(manga.getNome() + ": R$" + manga.getPreco());
        System.out.println(coca.getNome() + ": R$" + coca.getPreco());
        System.out.println(tepokki.getNome() + ": R$" + tepokki.getPreco());

        System.out.println("Preços com Desconto: ");
        System.out.println(manga.getNome() + ": R$" + getPrecoComDesconto(manga));
        System.out.println(coca.getNome() + ": R$" + getPrecoComDesconto(coca));
        System.out.println(tepokki.getNome() + ": R$" + getPrecoComDesconto(tepokki));
    }

    public static String getPrecoComDesconto(IGerarDesconto produto){
        return "R$" + produto.gerarPrecoComDesconto();
    }
}
