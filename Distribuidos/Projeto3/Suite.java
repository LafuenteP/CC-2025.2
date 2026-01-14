public class Suite extends Quarto {
    
    private boolean temJacuzzi;

    public Suite(int numero, int maxHospedes, double precoPorNoite, boolean temJacuzzi) {
        super(numero, maxHospedes, precoPorNoite);
        this.temJacuzzi = temJacuzzi;
    }

    public boolean isTemJacuzzi() {
        return temJacuzzi;
    }

    public void setTemJacuzzi(boolean temJacuzzi) {
        this.temJacuzzi = temJacuzzi;
    }
}