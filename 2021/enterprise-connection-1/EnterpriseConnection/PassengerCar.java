package EnterpriseConnection;

public class PassengerCar extends Car {
  
  public PassengerCar(String name) {
    super(name, CarType.PASSENGER);
  }

  public String toString() {
    return String.format("Carro de passageiro %s", name);
  }
}
