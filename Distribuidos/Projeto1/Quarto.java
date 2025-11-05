public abstract class Quarto {
    private int numero;
    private int maxHospedes;
    private double precoPorNoite;
    private boolean ocupado;

    public Quarto(int numero, int maxHospedes, double precoPorNoite) {
        this.numero = numero;
        this.maxHospedes = maxHospedes;
        this.precoPorNoite = precoPorNoite;
        this.ocupado = false; // Começa desocupado
    }

    // Getters
    public int getNumero() {
        return numero;
    }

    public int getMaxHospedes() {
        return maxHospedes;
    }

    public double getPrecoPorNoite() {
        return precoPorNoite;
    }

    public boolean isOcupado() {
        return ocupado;
    }

    // Setters
    public void setNumero(int numero) {
        this.numero = numero;
    }

    public void setMaxHospedes(int maxHospedes) {
        this.maxHospedes = maxHospedes;
    }

    public void setPrecoPorNoite(double precoPorNoite) {
        this.precoPorNoite = precoPorNoite;
    }

    public void setOcupado(boolean ocupado) {
        this.ocupado = ocupado;
    }

    @Override
    public String toString() {
        return "Quarto{" +
                "numero=" + numero +
                ", precoPorNoite=" + precoPorNoite +
                ", ocupado=" + ocupado +
                '}';
    }
}