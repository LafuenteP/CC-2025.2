public class QuartoSimples extends Quarto {
    
    private boolean temFrigobar;

    public QuartoSimples(int numero, int maxHospedes, double precoPorNoite, boolean temFrigobar) {
        super(numero, maxHospedes, precoPorNoite);
        this.temFrigobar = temFrigobar;
    }

    public boolean isTemFrigobar() {
        return temFrigobar;
    }

    public void setTemFrigobar(boolean temFrigobar) {
        this.temFrigobar = temFrigobar;
    }
}