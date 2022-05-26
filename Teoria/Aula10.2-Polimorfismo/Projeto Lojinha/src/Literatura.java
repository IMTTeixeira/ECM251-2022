public class Literatura extends Produto {
    private String editora;
    private String autor;
    private int paginas;
    private final EnumGeneroLiteratura genero;
    
    public Literatura(double preco, int quantidade, String descricao, String nome, String editora, String autor,
            int paginas, EnumGeneroLiteratura genero) {
        super(preco, quantidade, descricao, nome);
        this.editora = editora;
        this.autor = autor;
        this.paginas = paginas;
        this.genero = genero;
    }

    public String getEditora() {
        return editora;
    }

    public void setEditora(String editora) {
        this.editora = editora;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getPaginas() {
        return paginas;
    }

    public void setPaginas(int paginas) {
        this.paginas = paginas;
    }

    public EnumGeneroLiteratura getGenero() {
        return genero;
    }

    @Override
    public double gerarPrecoComDesconto() {
        return getPreco();
    }
}
