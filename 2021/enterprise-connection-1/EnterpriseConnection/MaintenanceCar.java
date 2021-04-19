package EnterpriseConnection;

public class MaintenanceCar extends Car {

  public MaintenanceCar(String name) {
    super(name, CarType.MAINTENANCE);
  }

  public String toString() {
    return String.format("Carro de manutenção %s", name);
  }
}

